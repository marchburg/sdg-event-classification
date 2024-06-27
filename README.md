# sdg-event-classification

This repository contains the data and scripts used for the classification of SDG-related events in sustainability reports. The repository includes the ground truth dataset, Python scripts for BERT fine-tuning, CatBoost and SHAP analysis, and LLM annotation.

## Table of Contents
- [sdg-event-classification](#sdg-event-classification)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Repository Structure](#repository-structure)
  - [Data Description](#data-description)
    - [Dataset Columns](#dataset-columns)
  - [Scripts and Usage](#scripts-and-usage)
    - [BERT Fine-Tuning](#bert-fine-tuning)
    - [CatBoost and SHAP Analysis](#catboost-and-shap-analysis)
    - [LLM Annotation](#llm-annotation)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Introduction
This repository aims to provide resources for the automated classification of events related to the Sustainable Development Goals (SDGs) in corporate sustainability reports. The provided dataset and scripts facilitate the replication of our study and enable further research in this domain.

## Repository Structure

SDG-Event-Classification/
├── data/
│   ├── ground_truth_train.csv
├── scripts/
│   ├── bert_fine_tuning.py
│   ├── catboost_shap.py
│   ├── llm_annotation.py
├── README.md
└── LICENSE


## Data Description
The `ground_truth_train.csv` and `ground_truth_train.csv` datasets contains annotated events extracted from sustainability reports. The `ground_truth_features_grouped_train.csv` and `ground_truth_features_grouped_test.csv` dataset contains only the feature values grouped for each event trigger. Train and test sets are split 70/30. Below is a description of each column in the dataset:

### Dataset Columns
- `document`: The identifier for the document from which the sentence was extracted.
- `text`: The full sentence from the document.
- `keyword`: The SDG-related keyword(s) identified within the sentence.
- `event_trigger`: The word or phrase indicating the occurrence of an event.
- `temporal_status`: The temporal status of the event (past, ongoing, future).
- `measurability`: A numerical value indicating how specific and quantifiable the event is.
- `event_factuality`: The event factuality level of the event, indicating its likelihood.
- `kw_is_nsubj`: A Boolean indicating if the keyword is a nominal subject.
- `kw_is_dobj`: A Boolean indicating if the keyword is a direct object.
- `kw_is_pobj`: A Boolean indicating if the keyword is a prepositional object.
- `category`: The classification of the event into categories action, intention, belief, or situation.
- `text_kw_et`: The sentence with the keyword and event trigger highlighted.
- `text_kw`: The sentence with the keyword highlighted.
- `relation_time_specification`: Temporal details related to the event (if any).
- `relation_unit`: The unit of measurement related to the event (if any).

## Scripts and Usage

### BERT Fine-Tuning
- **Script:** `bert_fine_tuning.py`
- **Description:** This script fine-tunes a BERT model on the annotated dataset to classify SDG-related events.
- **Usage:** Provide instructions on how to run the script, including command-line arguments and expected output.

### CatBoost and SHAP Analysis
- **Script:** `catboost_shap.py`
- **Description:** This script trains a CatBoost model on the event features and uses SHAP values to interpret feature importance.
- **Usage:** Provide instructions on how to run the script, including command-line arguments and expected output.

### LLM Annotation
- **Script:** `llm_annotation.py`
- **Description:** This script utilizes GPT-3.5 and GPT-4 models to annotate events in the dataset.
- **Usage:** Provide instructions on how to run the script, including command-line arguments and expected output.

## Installation
Instructions on how to set up the environment, including required dependencies and how to install them.

## Usage
Step-by-step instructions on how to use the dataset and scripts provided in the repository.

## Contributing
Guidelines for contributing to the repository.

## License
Details about the licensing of the repository.

## Contact
Contact information for questions and support.
