from prompts.tasks import tasks

SYSTEM_PROMPT_FEATURES = "You are an intelligent text classification expert system. Your task is to classify features of events in texts. I will provide you with the definition of the classification task, the definitions of the different classes, the input text for which you need to classify the event, along with a keyword and event trigger representing the event, and the output format. I will also provide you with examples, including the reasoning behind choosing a certain class. Please return the output strictly in JSON format, not prose."

SYSTEM_PROMPT_EVENT_TRIGGER = "You are an intelligent text classification expert system. Your task is to classify the event triggers in text that are related to a certain keyword. I will provide you with the definition of the task, the input text for which you need to classify the event trigger. I will also specify a keyword based on which you should choose the event trigger, and detail the output format. Additionally, I will provide you with examples, including the reasoning behind choosing a certain event trigger. Please return the output strictly in JSON format, not prose."

SYSTEM_PROMPT_EVENT_TRIGGER_CHAIN_OF_FEATURES = "You are an intelligent text classification expert system. Your initial task is to classify the event triggers in text that are related to a certain keyword. Your second task is to classify features of the event denoted by this keyword and event trigger. I will provide you with the definition of the tasks, the definitions of the different classes, the input text for which you need to classify the event trigger and the features of the event, along with a keyword, and the output format. I will also provide you with examples, including the reasoning behind choosing a certain event trigger or feature class. Please return the output strictly in JSON format, not prose."

SYSTEM_PROMPT_CHAIN_OF_FEATURES = "You are an intelligent text classification expert system. Your task is to classify features of the event denoted by this keyword and event trigger. I will provide you with the definition of the tasks, the definitions of the different classes, the input text for which you need to classify the features of the event, along with a keyword and event trigger representing the event, and the output format. I will also provide you with examples, including the reasoning behind choosing a certain feature class. Please return the output strictly in JSON format, not prose."

SYSTEM_PROMPT_INPUT_FEATURES = "You are an intelligent text classification expert system. Your task is to classify the category of events in text. I will provide you with the definition of the classification task, the definitions of the different classes, the input text for which you need to classify the event, along with a keyword and event trigger representing the event, and the output format. I will also provide you with examples, including the reasoning behind choosing a certain category. Additionally, I will provide you with a set of feature values for the event. For each of these event features, I will provide you with the definitions of the labels and examples. Before assigning the category to the event, inspect the provided feature values and consider their meaning for determining the category. Please return the output strictly in JSON format, not prose."

USER_PROMPT = "Are you clear about your role?"

ASSISTANT_PROMPT = "Sure, as an expert I'm ready to help you with your classification task. Please provide me with the necessary information to get started."

MAIN_PROMPT_TEMPLATE = """<s> [INST]
# Definitions: 

## Event trigger definition: 
An event trigger is a word or phrase, often a verb, that indicates an action or state. An event trigger usually relates to or affects at least one word or concept, typically a noun.
## Keyword definition: 
The keywords are spans of tokens related to one or more Sustainability Development Goals (SDG).
## Event definition:
The keyword along with the event trigger are part of what constitutes an event. There can be multiple events in one sentence. Additional words in the sentence may also be related to the event, or they might be important for classifying it. However, not all words in the sentence are directly related to the event or important for categorizing it.

# Task: 
{task_description}
Consider the context of the whole sentence when classifying the event. Avoid depending on implicit assumptions. Ground your decision in the information provided within the sentence.

# Label Definition: 
{label_definition}

# Output format:
Always respond in JSON format containing key-value pairs. Please ensure your output strictly follows this JSON format:
```json
{output_format}
```

# Examples:
{examples}

# Instructions:
{instructions}
[/INST]

Input: 
{input}

Analyze the above input with regards to the provided tasks and return a structured output in the required format as JSON, no prose.

Output:
"""

instructions_features = '''
Now it's your turn. The user provides you with a sentence along with a keyword and an event trigger that represent an event in the sentence. Classify the event according to the provided task description! Strictly adhere to the proposed JSON output format, no prose!
'''

instructions_event_trigger = '''
Now it's your turn. The user provides you with a sentence along with a keyword. Annotate the event trigger related to this keyword. Strictly adhere to the proposed JSON output format, no prose!
'''

instructions_event_trigger_cof = '''
Now it's your turn. The user provides you with a sentence along with a keyword. Annotate the event trigger related to this keyword. Then classify the event features according to the provided task description! Strictly adhere to the proposed JSON output format, no prose!
'''

instructions_input_features = '''
Now it's your turn. The user provides you with a sentence along with a keyword and an event trigger that represent an event in the sentence. The user will also provide you with a set of feature values for this event. Before assigning the category to the event, inspect the provided feature values and consider their meaning for determining the category. Classify the event according to the provided task description! Strictly adhere to the proposed JSON output format, no prose!
'''

def build_system_prompt(task_name):
    if task_name == "event_trigger":
        return SYSTEM_PROMPT_EVENT_TRIGGER
    elif task_name == "event_trigger_chain_of_features":
        return SYSTEM_PROMPT_EVENT_TRIGGER_CHAIN_OF_FEATURES
    elif task_name == "chain_of_features":
        return SYSTEM_PROMPT_CHAIN_OF_FEATURES
    elif task_name == "category_input_man_features" or task_name == "category_input_all_features":
        return SYSTEM_PROMPT_INPUT_FEATURES
    else:
        return SYSTEM_PROMPT_FEATURES

def build_user_prompt():
    return USER_PROMPT

def build_assistant_prompt():
    return ASSISTANT_PROMPT

def build_instructions(task_name):
    if task_name == "event_trigger":
        return instructions_event_trigger
    elif task_name == "event_trigger_chain_of_features":
        return instructions_event_trigger_cof
    else:
        return instructions_features

def build_main_prompt(task_name, text):
    task = tasks[task_name]

    instructions = build_instructions(task_name)

    main_prompt = MAIN_PROMPT_TEMPLATE.format(
        task_description=task["task_description"],
        label_definition=task["label_definition"],
        output_format=task["output_format"], 
        examples=task["examples"], 
        instructions=instructions,
        input=text
    )
    return main_prompt