# Resume Web Application
## Creator: John Walsh

#### This application displays my credentials for employment in a fun and occassionally interactive manner. For developing the application locally, it is reccomended to use pyenv + pipenv to create the local dev environment. This application also contains a simple text classification model built using pySpark. The model and transformation pipeline have been serialized and stored as files in the src/ directory of the project. The source code used to build and train the models will be released shortly.

## Installing the dev environment
#### In your favorite UNIX terminal run the following commands
```
git clone https://github.com/jrw34/JohnWalsh-Resume

cd JohnWalsh-Resume

pyenv local 3.13.0

pip install pipenv

pipenv install --dev

pipenv run pre-commit install
```

#### When changes are made to the codebase, be sure to run mypy and ruff and correct any errors before pushing to the repo
```
pipenv run ruff format
pipenv run ruff check
pipenv run mypy .
```

#### To locally run the application
```
pipenv run streamlit run src/resume_app.py
```

#### Note About Running Locally
##### When locally running the application, it is important that the proper version of Java is used. In order to ensure the Text Classification model properly configures the Spark environment, openjdk@17 should be used.

### Ingredient Identifier
 - CSV was downloaded from https://fdc.nal.usda.gov/download-datasets
 - File downloaded was "Full Download of All Data Types"
 - Size of File: approx. 3GB
 - File is cleaned and parsed then pushed to a cloud hosted AIVEN PostgreSQL instance
 - ETL steps are found in src/IngredientIdentifier/etl_tools/
 - To locally develop this application, the database url+key is required as a local environment variable
    - Add the url+key as DB_URL to .bashrc
 - If locally developing, an unzipped copy of the directory should be stored in the local repo
    - The location for the directory should be in src/IngredientIdentifier/