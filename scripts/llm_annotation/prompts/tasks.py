
event_trigger_task = {
"task_description": '''
Your task is to annotate the event trigger for a keyword. An event trigger is a word or phrase, often a verb, that indicates an action or state. Your task is to choose the event trigger that is most directly related to the keyword. You are answering the question, "What is happening to or with this keyword?". You need to assign at least one event trigger. One keyword can also relate to more than one event triggers.
Avoid relying on implicit assumptions in your determination. Ensure your decision is grounded in the information provided within the sentence.
''',
"label_definition": '''Please check the event trigger definition stated above.''', # TODO: check if content is needed here, a definition of et is given at beginning of each main prompt
"output_format": '''{"label": "your chosen event triggers as an array of String values extracted from the input sentence. An event trigger can be a single token or a sequence of tokens", "reasoning": "a concise explanation of your decision"}''',
"examples": '''
Input: "In the reporting period, Kordsa has activated reverse osmosis system at NY Yarn Facility and recycled 70,128 m3/year wastewater. (keyword: 'reverse osmosis system')"
Output: {"label": ["activated"], "reasoning": "'activated' is chosen as the event trigger for 'reverse osmosis system'. The event denoted by the keyword and event trigger is the activation or implementation of the reverse osmosis system, indicating the system was put into use or operation at the NY Yarn Facility."}

Input: "In the reporting period, Kordsa has activated reverse osmosis system at NY Yarn Facility and recycled 70,128 m3/year wastewater. (keyword: 'wastewater')"
Output: {"label": ["recycled"], "reasoning": "'recycled' is selected as the event trigger for 'wastewater' because it specifies the action performed on the wastewater. The event rdenoted by the keyword and event trigger is the recycling process of wastewater."}

Input: "CO2 emissions per net sales (organic, currency-adjusted) even declined by 5.6%. (keyword: 'CO2 emissions')"
Output: {"label": ["declined"], "reasoning": "'declined' is selected as the event trigger  because it explicitly indicates a change of state in the amount of CO2 emissions relative to net sales. The event denoted by the keyword and event trigger is the decrease in CO2 emissions."}

Input: "Another important stage on the way there is to change over our car plants in Germany to CO2-neutral energy supply by 2022. (keyword: 'CO2-neutral energy supply')"
Output: {"label": ["change"], "reasoning": "'change' is the event trigger for 'CO2-neutral energy supply' because it indicates the transition towards using a CO2-neutral energy source. The event denoted by the keyword and event trigger is the transition of car plants to CO2-neutral energy supply."}

Input: "The energy intensity, measured for the whole company by the metric of electric energy consumption divided by the number of own employees, was 13.50 in the year. (keyword: 'energy intensity')"
Output: {"label": ["was"], "reasoning": "'was' is chosen as the event trigger for 'energy intensity' because it describes the state or condition of the energy intensity metric within the company for a given period. The event denoted by the keyword and event trigger is the state of the energy intensity metric."}

Input: "The energy intensity, measured for the whole company by the metric of electric energy consumption divided by the number of own employees, was 13.50 in the year. (keyword: 'electric energy consumption')"
Output: {"label": ["measured", "reasoning": "'measured' is selected as the event trigger for 'electric energy consumption' as it denotes the action of quantifying the electric energy usage. The event denoted by the keyword and event trigger is the measurement of electric energy consumption."}

Input: "The principles of the Global Compact are a central frame of reference for our efforts, and the United Nations Sustainable Development Goals and the Paris Climate Agreement provide us with important impetus. (keyword: 'United Nations Sustainable Development Goals')"
Output: {"label": ["provide"], "reasoning": "'provide' is the event trigger for 'United Nations Sustainable Development Goals' because it describes the state of offering guidance or direction. The event denoted by the keyword and event trigger is the provision of guidance by the United Nations Sustainable Development Goals."}

Input: "In 2020 we have set a target to identify all risk suppliers and audit them. (keyword: 'risk suppliers')"
Output: {"label": "["identify", "audit"]", "reasoning": "'identify' and 'audit' are chosen as the event triggers for 'risk suppliers' because they describe the two distinct actions taken regarding these suppliers. The related events are the processes of identifying who the risk suppliers are and then conducting audits on them."}
'''
}

category_task = {
"task_description": '''
Your task is to assign one of four categories to the event in the sentence denoted by the event trigger and its related keyword. Consider the context of the whole sentence when determining the category. Avoid depending on implicit assumptions when determining the category. Ground your decision in the information provided within the sentence.
''',
"label_definition": '''
The event denoted by the event trigger and the related keyword is best described as:
action: Mention of an action, measure, initiative, or active engagement. The action should be described as either having been carried out in the past or as ongoing.
intention: Expression of a goal, plan, or intended outcome.
belief: Expression of a belief, value, philosophy, or ethos. This category emphasizes ideological standpoints rather than actions or plans.
situation: Description of a situation, state or progress. This category highlights a description of the situation or changes in the situation rather than actions, plans, or beliefs.
''',
"output_format": '''{"label": "your chosen category", "reasoning": "a concise explanation of your decision"}''',
"examples": '''
Input: "With the aim of achieving water savings, depressurizing systems and aerators that mix water with air are used in the taps Akbank branches. (keyword: 'depressurizing systems', event trigger: 'are used')"
Output: {"label": "action", "reasoning": "The event denoted here is the use of depressurizing systems at a certain location. It is an active measure carried out by an organization."}

Input: "We have doubled the representation of women in our senior manager population since 2011. (keyword: "representation of women", event trigger: "doubled")"
Output: {"label": "action", "reasoning": "This event is described as an action that has been carried out in the past. It indicates active engagement in increasing the representation of women in senior management."}

Input: "With the aim of achieving water savings, depressurizing systems and aerators that mix water with air are used in the taps Akbank branches. (keyword: "water savings", event trigger: "achieving")"
Output: {"label": "intention", "reasoning": "The event denoted by the keyword and event trigger is the achievement of water savings. It is presented as a goal with the phrase 'With the aim of' and does not imply a specific action per se."}

Input: "The goal is clear: Our products, and we as a company, must generally become more sustainable. (keyword: "sustainable", event trigger: "become")"
Output: {"label": "intention", "reasoning": "The transition towards greater sustainability in products and the company is stated here as a goal."}

Input: "In 2020 we have set a target to identify all risk suppliers and audit them. (keyword: "risk suppliers", event trigger: "audit")"
Output: {"label": "intention", "reasoning": "Even though the identification and auditing of risk suppliers is a concrete action, it is formulated as a goal still to be achieved."}

Input: "Manufacture of the products by Geberit accounts for only 8% of total CO2 emissions. (keyword: "CO2 emissions", event trigger: "accounts")"
Output: {"label": "situation", "reasoning": "The fact that a certain amount of CO2 emissions is accounted for by manufacturing is presented as a situation that an organisation finds itself in."}

Input: "Every employee of the company is subject to employees rules and regulations which include employees rights. (keyword: "employees rules", event trigger: "is subject to")"
Output: {"label": "situation", "reasoning": "Employees being subject to certain rules is presented as a situation independent of the organisation's intentions or beliefs."}

Input: "The principles of the Global Compact are a central frame of reference for our efforts. (keyword: "principles of the Global Compact", event trigger: "are")"
Output: {"label": "belief", "reasoning": "The principles of the Global Compact being a central frame of reference for the organisation's efforts is expressed as an ideological standpoint or a commitment to certain values or principles."}

Input: "Preserving jobs and dealing with necessary structural changes responsibly are important to us. (keyword: "jobs", event trigger: "Preserving")"
Output: {"label": "belief", "reasoning": "The phrase 'are important to us' indicates that the preservation of jobs is expressed as an ideological stance or a value judgment rather than describing a specific action being taken, a current situation, or a future intention."}
''',
}

temporal_status_task = {
"task_description": '''
Your task is to annotate the temporal status of the event associated with the keyword and the event trigger. Consider the context of the entire sentence when determining the temporal status. Avoid relying on implicit assumptions in your determination. Ensure your decision is grounded in the information provided within the sentence.
''',
"label_definition": '''
The temporal status of the event associated to the keyword and event trigger is:
past: An event that has started and has ended. There should be no reason to believe that it may still be in progress.
ongoing: An event that has started and is still in progress. There should be no reason to believe that it has ended.
future: An event that has not yet started. The context suggests that its occurrence is a possibility.
''',
"output_format": '''{"label": "your chosen temporal status", "reasoning": "a concise explanation of your decision"}''',
"examples": '''
Input: "As a long-time member of Transparency International Switzerland, Geberit is committed to high standards in combating corruption. (keyword: '', event trigger: 'is committed')"
Output: {"label": "ongoing", "reasoning": "The event related to the trigger is an ongoing commitment to maintaining high standards in combating corruption. There's no indication of a specific timeframe, suggesting a persistent and ongoing effort to combat corruption."}

Input: "In 2020 we have set a target to identify all risk suppliers and audit them. (keyword: '', event trigger: 'set')"
Output: {"label": "future", "reasoning": "Although the action of setting the target occurred in the past (as indicated by 'In 2020'), the specific act of identifying all at-risk suppliers, indicated by the event trigger 'identify,' is implied to take place in the future. The sentence lacks cues indicating whether the identification has already occurred by the time of writing, implying a future event."}

Input: "Honda will continue to examine the installation of a water recycling system around the world as necessary. (keyword: '', event trigger: 'will continue')"
Output: {"label": "future", "reasoning": "The phrasing 'will continue to examine' suggests that the action related to the event trigger, which is the installation of a water recycling system, is a prospective event that has not started but is being considered for implementation in the future."}

Input: "CO2 emissions per net sales (organic, currency-adjusted) even declined by 5.6%. (keyword: '', event trigger: 'declined')"
Output: {"label": "past", "reasoning": "The 5.6% decline of CO2 emissions is described as a completed event that occurred in the past."}
'''
}

measurability_task = {
"task_description": '''
Your task is to label the measurability of the event associated with the keyword and the event trigger, annotating it on a scale from 1 to 5. Consider the context of the entire sentence when determining the measurability level of the event. Avoid relying on implicit assumptions in your determination. Ensure your decision is grounded in the information provided within the sentence.
''',
"label_definition": '''
The event associated to the keyword and event trigger is:
1: Difficult or not possible to measure and quantify
2: Possible to measure and quantify
3: Quantified in the text with value OR time reference
4: Quantified in the text with value AND time reference
5: Quantified in the text comparing two values with time references
''',
"output_format": '''{"label": "your chosen measurability level", "reasoning": "a concise explanation of your decision"}''',
"examples": '''
Input: "We also recognize that diversity and inclusion challenges are unique to teams and locations. (keyword: 'diversity and inclusion challenges', event trigger: 'are')"
Output: {"label": "1", "reasoning": "Diversity and inclusion challenges being unique to teams and locations is a subjective and qualitative aspect. These challenges might vary based on subjective interpretations and contextual factors specific to each team, making them difficult to quantify or measure objectively."}

Input: "We make a meaningful contribution to the sustainability of the societies where we operate. (keyword: 'sustainability', event trigger: 'make')"
Output: {"label": "1", "reasoning": "The contribution to the sustainability of entire societies can hardly be quantified without reference to specific measures or targets."}

Input: "In addition, in the HO and ABC, photocell taps are used in WCs where water is used in great amounts, in order to achieve water savings. (keyword: 'water savings', event trigger: 'achieve')"
Output: {"label": "2", "reasoning": "The event triggered by 'achieve' pertains to the goal of achieving water savings. Although it doesn't provide a specific measure or value, it denotes a clear and quantifiable objective—reducing water consumption."}

Input: "Honda will continue to examine the installation of a water recycling system around the world as necessary. (keyword: 'water recycling system', event trigger: 'installation')"
Output: {"label": "2", "reasoning": "The installation of a water recycling system around the world outlines a quantifiable action without specifying any measures, units, or time references related to the actual installation of the water recycling system."}

Input: "CO2 emissions per net sales (organic, currency-adjusted) even declined by 5.6%. (keyword: 'CO2 emissions', event trigger: 'declined')"
Output: {"label": "3", "reasoning": "The decrease in CO2 emissions is provided with a clear quantitative measure '5.6%' related to the reduction in emissions. However, it lacks a specific time reference, such as when this decline occurred."}

Input: "Another important stage on the way there is to change over our car plants in Germany to CO2-neutral energy supply by 2022. (keyword: 'CO2-neutral energy supply', event trigger: 'change')"
Output: {"label": "3", "reasoning": "The transformation of car plants in Germany to CO2-neutral energy supply is supposed to happen within a specified timeframe ('by 2022')."}

Input: "In 2019, we conducted 69 supplier onsite audits plus co-operation meetings. (keyword: 'supplier onsite audits', event trigger: 'conducted')"
Output: {"label": "4", "reasoning": "The conduction of supplier onsite audits is specified with a concrete value and a time reference."}

Input: "By the end of 2020, our gender distribution across leadership positions was 80% men and 20% women, unchanged from 2019. (keyword: 'gender distribution', event trigger: 'was')"
Output: {"label": "5", "reasoning": "The event triggered by 'was' involves the gender distribution across leadership positions. This statement presents specific quantifiable values for the gender distribution at two different time points (2019 and the end of 2020). It involves a comparison of values between two time references."}
'''
}

relation_temp_task = {
"task_description": 
'''Your task is to annotate spans of words that specify the timing of an event. Only indicate time specifications if they occur in the sentence and refer to the event to which the event trigger and the keyword are related. There can be no, one, or multiple time specifications for an event. Avoid relying on implicit assumptions in your determination. Ensure your decision is grounded in the information provided within the sentence.
''',
"label_definition": '''
Definition of time specifications: Time specifications refer to numbers and words within the text that denote specific temporal information related to the event. These specifications include calendar dates, durations, time intervals, or temporal markers such as time-related adverbs. For example: "in 2020", "by the end of the year", "until 2030"
''',
"output_format": '''{"label": "Your chosen time specifictions from the input text. Empty string if there is no time specification for the given event. If there are multiple time specifications for an event, separate them by semikolon", "reasoning": "a concise explanation of your decision"}''',
"examples": '''
Input: "In 2019, we conducted 69 supplier onsite audits plus co-operation meetings. (keyword: 'onsite audits', event trigger: 'conducted')"
Output: {"label": "In 2019", "reasoning": "'In 2019' specifies the specific year when the supplier onsite audits were carried out, indicating that this event has already occurred."}

Input: "By the end of 2020, our gender distribution across leadership positions was 80% men and 20% women, unchanged from 2019. (keyword: 'gender distribution', event trigger: 'was')"
Output: {"label": "By the end of 2020; from 2019", "reasoning": "Both 'by the end of 2020' and 'from 2019' are time specifications related to the event denoted here, which is the state of the gender distribution across leadership, indicating a comparison of states at two different time points."}

Input: "In 2020 we have set a target to identify all risk suppliers and audit them. (keyword: 'risk suppliers', event trigger: 'identify')"
Output: {"label": "", "reasoning": "Although there is a time specification 'in 2020' in the sentence, it doesn't directly correlate with the event denoted by the event trigger and keyword. The sentence specifies that the target was set in 2020, but it doesn't explicitly indicate when the identification of risk suppliers will happen or by when it will be completed, suggesting an action with future implications."}

Input: "The goal is clear: Our products, and we as a company, must generally become more sustainable. (keyword: 'sustainable', event trigger: 'become')"
Output: {"label": "", "reasoning": "There is no time specification in this sentence, indicating an ongoing or future-oriented objective without a specified timeframe for achieving sustainability."}
'''
}

relation_quant_task = {
"task_description": '''
Your task is to annotate spans of words that quantify the event with a specific value. Only indicate quantified values if they occur in the sentence and refer to the event to which the event trigger and the keyword are related. There can be no, one, or multiple quantified values for an event. Avoid relying on implicit assumptions in your determination. Ensure your decision is grounded in the information provided within the sentence.
''',
"label_definition": '''
Definition of quantified values: A quantified value refers to a quantified or measured element in the sentence. This can include numerical measurements, percentages, quantities, or any other quantified information. The unit should be precise and directly tied to the event denoted by the event trigger and keyword.
''',
"output_format": '''{"label": "Your chosen quantified values from the input text. Empty string if there is no time specification for the given event. If there are multiple time specifications for an event, separate them by semikolon", "reasoning": "a concise explanation of your decision"}''',
"examples": '''
Input: "The share of purchased green electricity increased from 23.4 GWh to 41.0 GWh in 2015. (keyword: 'green electricity', event trigger: 'increased')"
Output: {"label": "23.4 GWh; 41.0 GWh", "reasoning": "The increase of the share of purchased green electricity is quantified by the two values '23.4 GWh' and '41.0 GWh'."}

Input: "CO2 emissions per net sales (organic, currency-adjusted) even declined by 5.6%. (keyword: 'CO2 emissions', event trigger: 'declined')"
Output: {"label": "5.6%", "reasoning": "The decline of CO2 emissions is quantified by the value 5.6%."}

Input: "Over the past five years, Accenture and Save the Children have partnered to skill more than 38,000 disadvantaged youth in a dozen countries, including Indonesia and the Philippines. (keyword: 'disadvantaged youth', event trigger: 'skill')"
Output: {"label": "more than 38,000", "reasoning": "The providing of skill to the disadvantaged youth is quantified by 'more than 38,000'."}

Input: "In the reporting period, Kordsa has activated reverse osmosis system at NY Yarn Facility and recycled 70,128 m3/year wastewater. (keyword: 'reverse osmosis system', event trigger: 'activated')"
Output: {"label": "", "reasoning": "Even though there is a value mentioned in the sentence, '70,128 m3/year,' it is not directly associated with the activation of the reverse osmosis system. Therefore, no value is selected for the given event trigger and keyword."}

Input: "Honda strives to reduce environmental impact during product usage. (keyword: 'environmental impact', event trigger: 'strives')"
Output: {"label": "", "reasoning": "There is no quantified value in this sentence. Therefore, none was selected."}
'''
}


chain_of_features_task = {
"task_description": f'''
Your main task is to assign one of four categories to the event in the sentence denoted by the event trigger and its related keyword. Before assigning the category class to the event, you need to determine the temporal status of the event, the measurability of the event, time specifications, and quantified values related to the event. Consider the context of the whole sentence when determining the temporal status, measurability, time specifications, quantified values, and category. Avoid depending on implicit assumptions. Ground your decision in the information provided within the sentence.

I will provide you with the definition of each classification task and the definitions of the different classes. I will also provide you with examples, including the reasoning behind choosing a certain class.

## Temporal Status:
### Task Description:
{temporal_status_task["task_description"]}
### Examples:
{temporal_status_task["examples"]}
### Output format:
Choose this output format as the value for the key "temporal_status" in the final output:
{temporal_status_task["output_format"]}

## Time Specifications:
### Task Description:
{relation_temp_task["task_description"]}
### Examples:
{relation_temp_task["examples"]}
### Output format:
Choose this output format as the value for the key "time_specifications" in the final output:
{relation_temp_task["output_format"]}

## Quantified Values:
### Task Description:
{relation_quant_task["task_description"]}
### Examples:
{relation_quant_task["examples"]}
### Output format:
Choose this output format as the value for the key "quantified_values" in the final output:
{relation_quant_task["output_format"]}

## Measurability:
### Task Description:
{measurability_task["task_description"]}
### Examples:
{measurability_task["examples"]}
### Output format:
Choose this output format as the value for the key "measurability" in the final output:
{measurability_task["output_format"]}

## Category:
### Task Description:
{category_task["task_description"]}
### Label Definition:
{category_task["label_definition"]}
### Examples:
{category_task["examples"]}

''',
"label_definition": '''
A dictionary with the following keys: 'temporal_status', 'time_specifications', 'quantified_values', 'measurability', 'category'. The value for each key is the output format of the corresponding subtask.
''',
"output_format": f'''{{"temporal_status": {temporal_status_task['output_format']}, "time_specifications": {relation_temp_task['output_format']}, "quantified_values": {relation_quant_task['output_format']}, "measurability": {measurability_task['output_format']}, "category": {category_task['output_format']}}}''',
"examples": f'''Inspect the examples for the subtasks. Create a dictionary with the label and reasoning for each subtask as described in the output format''',
"subtasks": ['temporal_status', 'time_specifications', 'quantified_values', 'measurability', 'category']
}


event_trigger_chain_of_features_task = {
"task_description": f'''
## Event Trigger:
### Task Description:
Your initial task is to annotate the event trigger for the given keyword: 
{event_trigger_task["task_description"]}
### Examples:
{event_trigger_task["examples"]}
### Output format:
Choose this output format as the value for the key "event_trigger" in the final output:
{event_trigger_task["output_format"]}

# Task:
{chain_of_features_task["task_description"]}
''',
"label_definition": '''
A dictionary with the following keys: 'event_trigger', 'temporal_status', 'time_specifications', 'quantified_values', 'measurability', 'category'. The value for each key is the output format of the corresponding subtask.
''',
"output_format": f'''{{"event_trigger": {event_trigger_task['output_format']}, "temporal_status": {temporal_status_task['output_format']}, "time_specifications": {relation_temp_task['output_format']}, "quantified_values": {relation_quant_task['output_format']}, "measurability": {measurability_task['output_format']}, "category": {category_task['output_format']}}}''',
"examples": f'''Inspect the examples for the subtasks. Create a dictionary with the label and reasoning for each subtask as described in the output format''',
"subtasks": ['event_trigger', 'temporal_status', 'time_specifications', 'quantified_values', 'measurability', 'category']
}

# ------------------------------------------------------------
# --- input is feature values and text, output is category ---
# ------------------------------------------------------------

input_features_initial_string = "The following sections describe the event feature values that are provided along with the input sentence, the keyword, and the event trigger."

category_input_man_features_task = {
"task_description": f'''
{input_features_initial_string}

## Temporal Status:
### Label Definition:
{temporal_status_task["label_definition"]}
### Examples
{temporal_status_task["examples"]}

## Time Specifications:
### Label Definition:
{relation_temp_task["label_definition"]}
### Examples
{relation_temp_task["examples"]}

## Quantified Values:
### Label Definition:
{relation_quant_task["label_definition"]}
### Examples
{relation_quant_task["examples"]}

## Measurability:
### Label Definition:
{measurability_task["label_definition"]}
### Examples
{measurability_task["examples"]}

## Category:
### Task Description:
{category_task['task_description']}
### Label Definition:
{category_task["label_definition"]}
''',
"label_definition": category_task["label_definition"],
"output_format": category_task["output_format"],
"examples": '''
Input: "With the aim of achieving water savings, depressurizing systems and aerators that mix water with air are used in the taps Akbank branches. (keyword: 'depressurizing systems', event trigger: 'are used', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '2')"
Output: {"label": "action", "reasoning": "The event denoted here is the use of depressurizing systems at a certain location. It is an active measure carried out by an organization."}

Input: "We have doubled the representation of women in our senior manager population since 2011. (keyword: 'representation of women', event trigger: 'doubled', temporal status: 'past', time specifications: 'since 2011', quantified values: 'doubled', measurability: '5')"
Output: {"label": "action", "reasoning": "This event is described as an action that has been carried out in the past. It indicates active engagement in increasing the representation of women in senior management."}

Input: "With the aim of achieving water savings, depressurizing systems and aerators that mix water with air are used in the taps Akbank branches. (keyword: 'water savings', event trigger: 'achieving', temporal status: 'future', time specifications: '', quantified values: '', measurability: '2')"
Output: {"label": "intention", "reasoning": "The event denoted by the keyword and event trigger is the achievement of water savings. It is presented as a goal with the phrase 'With the aim of' and does not imply a specific action per se."}

Input: "The goal is clear: Our products, and we as a company, must generally become more sustainable. (keyword: 'sustainable', event trigger: 'become', temporal status: 'future', time specifications: '', quantified values: '', measurability: '1')"
Output: {"label": "intention", "reasoning": "The transition towards greater sustainability in products and the company is stated here as a goal."}

Input: "In 2020 we have set a target to identify all risk suppliers and audit them. (keyword: 'risk suppliers', event trigger: 'audit', temporal status: 'future', time specifications: '', quantified values: 'all', measurability: '3')"
Output: {"label": "intention", "reasoning": "Even though the identification and auditing of risk suppliers is a concrete action, it is formulated as a goal still to be achieved."}

Input: "Manufacture of the products by Geberit accounts for only 8% of total CO2 emissions. (keyword: 'CO2 emissions', event trigger: 'accounts', temporal status: 'ongoing', time specifications: '', quantified values: '8%', measurability: '3')"
Output: {"label": "situation", "reasoning": "The fact that a certain amount of CO2 emissions is accounted for by manufacturing is presented as a situation that an organisation finds itself in."}

Input: "Every employee of the company is subject to employees rules and regulations which include employees rights. (keyword: 'employees rules', event trigger: 'is subject to', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '2')"
Output: {"label": "situation", "reasoning": "Employees being subject to certain rules is presented as a situation independent of the organisation's intentions or beliefs."}

Input: "The principles of the Global Compact are a central frame of reference for our efforts. (keyword: 'principles of the Global Compact', event trigger: 'are', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '1')"
Output: {"label": "belief", "reasoning": "The principles of the Global Compact being a central frame of reference for the organisation's efforts is expressed as an ideological standpoint or a commitment to certain values or principles."}

Input: "Preserving jobs and dealing with necessary structural changes responsibly are important to us. (keyword: 'jobs', event trigger: 'Preserving', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '1')"
Output: {"label": "belief", "reasoning": "The phrase 'are important to us' indicates that the preservation of jobs is expressed as an ideological stance or a value judgment rather than describing a specific action being taken, a current situation, or a future intention."}
''',
}

category_input_all_features_task = {
"task_description": f'''
{input_features_initial_string}

## Event Factuality:
Event factuality prediction is the process of estimating the factuality of events in texts. The goal is to recognize whether event mentions in texts represent actual situations in the world, situations that have not happened, or situations of uncertain interpretation where occurrence is a possibility. An event factuality score is defined for possible event triggers.

### Label Definition:
The labels are defined as follows:
-1_negative: Events that are stated as not having occurred or events that are surrounded by a high degree of negativity or doubt regarding their occurrence.
0_low: Events with a low level of certainty; there is a significant level of uncertainty or minimal commitment to the event's occurrence.
1_medium: Events with a moderate level of certainty; the language used to describe these events suggests a more than average likelihood or belief in their occurrence but stops short of full affirmation.
2_high: Events with a high level of certainty expressed about their occurrence, but not with the absolute certainty that characterizes the max level.
3_max: Events that are stated with the maximum level of certainty to have definitely occurred, with no ambiguity or doubt expressed.

### Examples
The following examples show the Tokens of sentences and event factuality scores assigned to them.

Example 1:
tokens: ["New", "evidence", "is", "suggesting", "that", "a", "series", "of", "bombings", "in", "Atalanta", "and", "last", "month", "'s", "explosion", "at", "an", "Alabama", "women", "'s", "clinic", "might", "be", "related", "."]
event_factuality: ["_", "_", "_", "2_high", "_", "_", "_", "_", "3_max", "_", "_", "_", "_", "_", "_", "3_max", "_", "_", "_", "_", "_", "_", "_", "_", "0_low", "_"]

Example 2: 
tokens: ["A", "bomb", "blast", "shocks", "the", "Olympic", "games", "."], 
event_factuality: ["_", "2_high", "3_max", "3_max", "_", "_", "2_high", "_"]
    
Example 3:
tokens: ["Steel", "plates", "recovered", "at", "the", "Olympic", "park", "bombing", "appear", "to", "match", "those", "found", "at", "the", "abortion", "clinic", "bombing", "in", "Atlanta", "."], event_factuality: ["_", "_", "3_max", "_", "_", "_", "_", "3_max", "_", "_", "0_low", "_", "3_max", "_", "_", "_", "_", "_", "_", "_"]

Example 4: tokens: ["And", "nails", "found", "in", "the", "Atlanta", "abortion", "clinic", "bombing", "are", "identical", "to", "those", "discovered", "at", "Rudolph", "'s", "storage", "shed", "in", "north", "Carolina", "."]
event_factuality: ["_", "_", "3_max", "_", "_", "_", "1_medium", "_", "3_max", "_", "_", "_", "_", "3_max", "_", "_", "_", "_", "_", "_", "_"]

Example 5: tokens: ["A", "senior", "law", "enforcement", "source", "tells", "CNN", ",", "there", "is", "a", "lot", "of", "circumstantial", "evidence", "and", "it", "would", "be", "extraordinary", "to", "have", "all", "these", "bits", "and", "pieces", "and", "there", "not", "be", "a", "connection", "."]
event_factuality: ["_", "_", "_", "1_medium", "_", "3_max", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "-1_negative", "_"]

Example 6: tokens: ["And", "law", "enforcement", "sources", "say", "they", "ca", "n't", "ignore", "letters", "penned", "under", "the", "name", "army", "of", "god", "."]
event_factuality: ["_", "_", "_", "_", "3_max", "_", "_", "_", "-1_negative", "_", "2_high", "_", "_", "_", "_", "_", "_"]

## Dependency Relation
Dependency relations characterize how words in a sentence are syntactically related to one another. Specifically, this feature determines whether a keyword serves as the subject, direct object, or prepositional object in the sentence.

### Label Definition:
kw_is_nsubj: This label is True if the keyword functions as the nominative subject (nsubj) of the sentence. The nominative subject is typically the entity performing the action or the entity that the sentence is about.
kw_is_dobj: This label is True if the keyword acts as the direct object (dobj) in the sentence. The direct object is usually the recipient of the action or the entity that is being acted upon.
kw_is_pobj: This label is True if the keyword operates as the prepositional object (pobj) within the sentence. The prepositional object is the entity that is related to another element of the sentence by a preposition.

### Examples:
Example 1:
The energy intensity, measured for the whole company by the metric of electric energy consumption divided by the number of own employees, was 13.50 in the year. (keyword: "The energy intensity", kw_is_nsubj: "True", kw_is_dobj: "False", kw_is_pobj: "False")

Example 1:
The energy intensity, measured for the whole company by the metric of electric energy consumption divided by the number of own employees, was 13.50 in the year. (keyword: "The energy intensity", kw_is_nsubj: "True", kw_is_dobj: "False", kw_is_pobj: "False")

Example 2:
In the reporting period, Kordsa has activated reverse osmosis system at NY Yarn Facility and recycled 70,128 m3/year wastewater. (keyword: "reverse osmosis system", kw_is_nsubj: "False", kw_is_dobj: "True", kw_is_pobj: "False")

Example 3:
As a long-time member of Transparency International Switzerland, Geberit is committed to high standards in combating corruption. (keyword: "Transparency International Switzerland", kw_is_nsubj: "False", kw_is_dobj: "False", kw_is_pobj: "True")

{category_input_man_features_task["task_description"]}
''',
"label_definition": category_task["label_definition"],
"output_format": category_task["output_format"],
"examples": '''
Input: "With the aim of achieving water savings, depressurizing systems and aerators that mix water with air are used in the taps Akbank branches. (keyword: 'depressurizing systems', event trigger: 'are used', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '2', event_factuality: '3_max', kw_is_nsubj: "False", kw_is_dobj: "False", kw_is_pobj: "False")"
Output: {"label": "action", "reasoning": "The event denoted here is the use of depressurizing systems at a certain location. It is an active measure carried out by an organization."}

Input: "We have doubled the representation of women in our senior manager population since 2011. (keyword: 'representation of women', event trigger: 'doubled', temporal status: 'past', time specifications: 'since 2011', quantified values: 'doubled', measurability: '5', event_factuality: '3_max', kw_is_nsubj: "False", kw_is_dobj: "True", kw_is_pobj: "True")"
Output: {"label": "action", "reasoning": "This event is described as an action that has been carried out in the past. It indicates active engagement in increasing the representation of women in senior management."}

Input: "With the aim of achieving water savings, depressurizing systems and aerators that mix water with air are used in the taps Akbank branches. (keyword: 'water savings', event trigger: 'achieving', temporal status: 'future', time specifications: '', quantified values: '', measurability: '2', event_factuality: '0_low', kw_is_nsubj: "False", kw_is_dobj: "True", kw_is_pobj: "False")"
Output: {"label": "intention", "reasoning": "The event denoted by the keyword and event trigger is the achievement of water savings. It is presented as a goal with the phrase 'With the aim of' and does not imply a specific action per se."}

Input: "The goal is clear: Our products, and we as a company, must generally become more sustainable. (keyword: 'sustainable', event trigger: 'become', temporal status: 'future', time specifications: '', quantified values: '', measurability: '1', event_factuality: '0_low', kw_is_nsubj: "False", kw_is_dobj: "False", kw_is_pobj: "False")"
Output: {"label": "intention", "reasoning": "The transition towards greater sustainability in products and the company is stated here as a goal."}

Input: "In 2020 we have set a target to identify all risk suppliers and audit them. (keyword: 'risk suppliers', event trigger: 'audit', temporal status: 'future', time specifications: '', quantified values: 'all', measurability: '3', event_factuality: '0_low', kw_is_nsubj: "False", kw_is_dobj: "True", kw_is_pobj: "False")"
Output: {"label": "intention", "reasoning": "Even though the identification and auditing of risk suppliers is a concrete action, it is formulated as a goal still to be achieved."}

Input: "Manufacture of the products by Geberit accounts for only 8% of total CO2 emissions. (keyword: 'CO2 emissions', event trigger: 'accounts', temporal status: 'ongoing', time specifications: '', quantified values: '8%', measurability: '3', event_factuality: '3_max', kw_is_nsubj: "False", kw_is_dobj: "False", kw_is_pobj: "True")"
Output: {"label": "situation", "reasoning": "The fact that a certain amount of CO2 emissions is accounted for by manufacturing is presented as a situation that an organisation finds itself in."}

Input: "Every employee of the company is subject to employees rules and regulations which include employees rights. (keyword: 'employees rules', event trigger: 'is subject to', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '2', event_factuality: '3_max', kw_is_nsubj: "False", kw_is_dobj: "False", kw_is_pobj: "True")"
Output: {"label": "situation", "reasoning": "Employees being subject to certain rules is presented as a situation independent of the organisation's intentions or beliefs."}

Input: "The principles of the Global Compact are a central frame of reference for our efforts. (keyword: 'principles of the Global Compact', event trigger: 'are', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '1', event_factuality: '3_max', kw_is_nsubj: "True", kw_is_dobj: "False", kw_is_pobj: "False")"
Output: {"label": "belief", "reasoning": "The principles of the Global Compact being a central frame of reference for the organisation's efforts is expressed as an ideological standpoint or a commitment to certain values or principles."}

Input: "Preserving jobs and dealing with necessary structural changes responsibly are important to us. (keyword: 'jobs', event trigger: 'Preserving', temporal status: 'ongoing', time specifications: '', quantified values: '', measurability: '1', event_factuality: '0_low', kw_is_nsubj: "False", kw_is_dobj: "True", kw_is_pobj: "False")"
Output: {"label": "belief", "reasoning": "The phrase 'are important to us' indicates that the preservation of jobs is expressed as an ideological stance or a value judgment rather than describing a specific action being taken, a current situation, or a future intention."}
''',
}

# The dictionary with all the tasks
tasks = {
    "event_trigger" : event_trigger_task,
    "category" : category_task,
    "temporal_status" : temporal_status_task,
    "measurability" : measurability_task,
    "relation_temp" : relation_temp_task,
    "relation_quant" : relation_quant_task,
    "chain_of_features" : chain_of_features_task,
    "event_trigger_chain_of_features" : event_trigger_chain_of_features_task,
    "category_input_man_features" : category_input_man_features_task,
    "category_input_all_features" : category_input_all_features_task,
}
