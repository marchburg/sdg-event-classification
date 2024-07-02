import openai
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import json
import pandas as pd
import os
from datetime import datetime

# Load environment variables from .env file (such as OPENAI_API_KEY)
_ = load_dotenv(find_dotenv())

from prompts.template import build_system_prompt, build_user_prompt, build_assistant_prompt, build_main_prompt
from prompts.tasks import tasks

def classify_event(client, model, task_name, text):

    system_prompt = build_system_prompt(task_name)
    user_prompt = build_user_prompt()
    assistant_prompt = build_assistant_prompt()
    main_prompt = build_main_prompt(task_name, text)

    # print(f'{task_name} - {text}')
    # print(f'\n{system_prompt}')
    # print(f'\n{user_prompt}')
    # print(f'\n{assistant_prompt}')
    # print(f'\n{main_prompt}')

    # create a response
    response = client.chat.completions.create(
        model=model,
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": assistant_prompt},
            {"role": "user", "content": main_prompt}
        ],
    )
    return (response.choices[0].message.content)


# -------------------------------
# -- test with single sentence --
# -------------------------------

# test_input_kw_et_man = "The Company is fully committed to ensuring that its employees are treated equally, irrespective of gender, ethnic origin, disability, marital status, political opinion, nationality, religion, sexual orientation or age. (keyword: 'sexual orientation', event trigger: 'treated', temporal_status: 'ongoing', time specifications: '', quantified values: '', measurability: '1')"
# test_input_kw_et = "The Company is fully committed to ensuring that its employees are treated equally, irrespective of gender, ethnic origin, disability, marital status, political opinion, nationality, religion, sexual orientation or age. (keyword: 'sexual orientation', event trigger: 'treated')"
# test_input_kw = "The Company is fully committed to ensuring that its employees are treated equally, irrespective of gender, ethnic origin, disability, marital status, political opinion, nationality, religion, sexual orientation or age. (keyword: 'sexual orientation')"

# # response = classify_event('category_input_man_features', test_input_kw_et_man)
# # response = classify_event('event_trigger_chain_of_features', test_input_kw)
# # response = classify_event('chain_of_features', test_input_kw_et)
# response = classify_event('category', test_input_kw_et)
# response_json = json.loads(response)
# print(response_json)

# -------------------------


def select_input_text(row, task_name):
    '''
    Select the input text for the specified task
    row: dataframe row
    task_name: task name as specified in the tasks dictionary
    '''
    if task_name == 'event_trigger' or task_name == 'event_trigger_chain_of_features':
        return row['text_kw']
    elif task_name == 'category_input_man_features':
        return row['text_kw_et_man']
    elif task_name == 'category_input_all_features':
        return row['text_kw_et_all']
    else:
        return row['text_kw_et']
    

def initialize_response_columns(df, task_names, model):
    """
    Initialize columns for storing classification results.
    """
    for task_name in task_names:

        if task_name in ['chain_of_features', 'event_trigger_chain_of_features']:

            cof_task_name = 'cof' if task_name == 'chain_of_features' else 'et_cof'

            # Subtasks are defined in a global `tasks` dictionary
            subtasks = tasks[task_name]["subtasks"]

            for subtask_name in subtasks:
                df[f'{model}_{cof_task_name}_{subtask_name}_label'] = None
                df[f'{model}_{cof_task_name}_{subtask_name}_reasoning'] = None
        else:
            df[f'{model}_{task_name}_label'] = None
            df[f'{model}_{task_name}_reasoning'] = None

    return df


def handle_standard_response(df, response, index, model, task_name):
    '''
    Handle response for standard tasks without nested dictionaries.
    '''
    # Check if 'label' and 'reasoning' are in the response
    if 'label' in response and 'reasoning' in response:
        df.at[index, f'{model}_{task_name}_label'] = response['label']
        df.at[index, f'{model}_{task_name}_reasoning'] = response['reasoning']
    else:
        print(f"Missing 'label' or 'reasoning' in response for row {index} and task '{task_name}'.")


def handle_chain_of_features_response(df, response, index, model, task_name):
    '''
    Handle response for "chain_of_features" task with nested dictionaries.
    '''
    cof_task_name = 'cof' if task_name == 'chain_of_features' else 'et_cof'
    for subtask_name, subtask_response in response.items():
        # Skip handling if the subtask response is not as expected
        if not isinstance(subtask_response, dict) or 'label' not in subtask_response or 'reasoning' not in subtask_response:
            print(f"Unexpected format in subtask response for '{subtask_name}' in row {index}.")
            continue
        # Save the classification results
        df.at[index, f'{model}_{cof_task_name}_{subtask_name}_label'] = subtask_response.get('label', None)
        df.at[index, f'{model}_{cof_task_name}_{subtask_name}_reasoning'] = subtask_response.get('reasoning', None)

def classify_df(task_names, df, client, model):
    '''
    Classify the events in the dataframe using the specified tasks
    task_names: list of task names as specified in the tasks dictionary
    df: dataframe with the input data
    '''
    # Initialize columns for storing results
    df = initialize_response_columns(df, task_names, model)

    # Classify the events in the dataframe
    for task_name in task_names:

        # Iterate over the rows in the dataframe
        for index, row in df.iterrows():

            # Select the input text for the task
            input_text = select_input_text(row, task_name)

            # Get the model response
            response = classify_event(client, model, task_name, input_text)

            print(f'{task_name} - {row["document"]}\n{response}' )

            # Safely parse the response
            try:
                response = json.loads(response)
            except json.JSONDecodeError:
                print(f"Error decoding JSON response for row {index} and task '{task_name}'.")
                continue

            # Handle response for "chain_of_features" task with nested dictionaries
            if task_name in ['chain_of_features', 'event_trigger_chain_of_features']:
                handle_chain_of_features_response(df, response, index, model, task_name)
            else:
                # Standard tasks with direct response handling
                handle_standard_response(df, response, index, model, task_name)

    return df


def load_input_data(data_folder_path):
    '''
    Load the input data from a CSV file.
    input_path: path to the input CSV file
    '''
    df_train = pd.read_csv(f'{data_folder_path}/ground_truth_train.csv')
    df_test = pd.read_csv(f'{data_folder_path}/ground_truth_test.csv')
    # combine the train and test data
    df = pd.concat([df_train, df_test])
    return df


def main():

    # Load the input data
    df_input = load_input_data('../../data')

    # df_select = df_input.copy()
    df_select = df_input.sample(4).copy() # for testing

    # Select the annotation tasks
    selected_tasks = tasks.keys()

    # initialize the openai client
    client = OpenAI()

    model = "gpt-3.5-turbo-0125"
    # model = "gpt-4-0125-preview"

    # classify the events
    df_gpt = classify_df(selected_tasks, df_select, client, model)

    # save the output
    current_date = datetime.now().strftime("%y%m%d")
    output_path = f'output/{model}/{current_date}/ground_truth_llm.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_gpt.to_csv(output_path, index=False)
