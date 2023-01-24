# GPT-3 Sandbox: Generate SQL Queries from Natural Language
## Description

This repository contains a Python module that allows you to easily interact with the OpenAI API. It is designed to be as simple as possible to use, and to allow for rapid prototyping of ideas. It is also designed to be extensible, so that you can easily add your own examples and create your own modules.
The file gpt3-sql-demo.py contains a working example of how to use the module to generate SQL queries from natural language.
## Requirements

Coding-wise, you only need Python. But for the app to run, you will need:

* API key from the OpenAI API beta invite
* Python 3
* `yarn`
* Node 16

## Setup

First, clone or fork [this](https://github.com/shreyashankar/gpt3-sandbox) repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`. I used the default name `venv` for my virtual environment.
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Run `python3 -m pip install openai` to install the OpenAI API wrapper. 
4. Run `python3 -m pip install python-dotenv` to install the dotenv package.
5. Install requirements: `pip install -r api/requirements.txt`
6. To add your secret key: create a file under `api` called `.env` with the contents `OPENAI_API_KEY=$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (including quotes). If you are unsure what your secret key is, navigate to the [API Keys page](https://beta.openai.com/account/api-keys) and click "Copy" next to a token displayed under "Secret Key". If there is none, click on "Create new secret key" and then copy it.
7. Set your environment variable to read the secret key: run `export OPENAI_CONFIG=.env` (for MacOS, Unix, or Linux users) or `set OPENAI_CONFIG=.env` (for Windows users)
8. Run `yarn install` in the root directory. Note: If you do not have yarn installed, you can install it by running `npm install --global yarn`. If this throws any errors, delete the `yarn.lock` file and try again. For macos users, you may run `brew install yarn` instead.

## Running the app
`python3 gpt3-sandbox.py`