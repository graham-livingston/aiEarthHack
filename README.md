# Mr.Business #

## Overview
This repository contains a collection of files for a web-based dashboard project, utilizing Flask for the backend, with a focus on NLP (Natural Language Processing) for identifying promising business ideas. The project is designed to provide an interactive user interface for the submission and review of business ideas, offering insights into their relevance and potential.

## File Descriptions

flask_session/: This directory likely contains session-related data for users interacting with the Flask application.

templates/: Holds HTML templates for the Flask application. The templates define the structure and layout of the web pages displayed to the users.

.env: A dotenv file for setting environment variables that the Flask application uses, such as database URLs, secret keys, etc. This file was updated recently to include dashboard configurations.

NLP_Model.ipynb: A Jupyter notebook containing the methodology for the NLP model used to identify promising business ideas. It includes the model's code, comments, and possibly visualization of the data and results.

README.md: This file provides an overview and documentation for the repository. It was the initial file committed to the repository.

app.py: The main Flask application file. It includes the routes and views for the dashboard.

clean.py: A Python script that was added to the repository early on. Its purpose is likely for data cleaning operations.

cleandata.csv: A CSV file containing data that has been cleaned, presumably for use in the application or NLP model.

data.csv: The original dataset file. It might be the raw data that goes through the cleaning process.

functions.py: Contains Python functions that support the dashboard functionality. These might include helper functions, data processing functions, etc.

prompt.py: A Python file related to the dashboard, possibly handling the creation and management of prompts within the application.

requirements.txt: Lists all the Python dependencies needed for the project. This file is crucial for setting up the project environment.

test.json: A JSON file that may include test data or configurations for the dashboard.

testing.ipynb: A Jupyter notebook for testing different components of the project, such as data processing, model performance, etc.

