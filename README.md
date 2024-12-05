# Resume Web Application
## Creator: John Walsh

#### This application displays my credentials for employment in a fun and occassionally interactive manner. For developing the application locally, it is reccomended to use pyenv + pipenv to create the local dev environment. This application also contains a simple text classification model built using pySpark. The model and transformation pipeline have been serialized and stored as files in the home directory of the project. The source code used to build and train the models will be released shortly. 

## Installing the dev environment
#### In your favorite UNIX terminal run the following commands
```
git clone https://github.com/jrw34/JohnWalsh-Resume

cd JohnWalsh-Resume

pyenv local 3.13.0

pip install pipenv

pipenv install
```

#### To locally run the application
```
pipenv run streamlit run src/resume_app.py
```