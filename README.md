# Question Answering API
> 🤗 Huggingface + ⚡ FastAPI = ❤️ Receive context and question returns answers


How to server Hugging face models with FastAPI, the Python's fastest API framework. 

Project structure for development and production. 

Installation and setup instructions to 
run the development mode model and serve a local RESTful API endpoint.

## Requirements

Python 3.6+

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).
<!-- ```bash
pip install -r requirements
```  -->

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Runnning Easter Egg

`make easter`


## Setup
1. Duplicate the `.env.example` file and rename it to `.env` 


2. In the `.env` file configure the `API_KEY` entry. The key is used for authenticating our API. <br>
   Execute script to generate .env, and replace `example_key`with the UUID generated:
```bash
make generate_dot_env
python -c "import uuid;print(str(uuid.uuid4()))"

```


## Run It

1. Start your  app with: 
```bash
uvicorn huggingfastapi.main:app
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs) or  [http://localhost:8000/redoc](http://localhost:8000/redoc) for alternative swagger
   
3. Click `Authorize` and enter the API key as created in the Setup step.

   
## Run Tests

If you're not using `tox`, please install with:
```bash
pip install tox pytest flake8 coverage bandit
```

Run your tests with: 
```bash
tox
```

This runs tests and coverage for Python 3.8 and Flake8, Bandit.

## Project structure

Files related to application are in the `huggingfastapi` or `tests` directories.
Application parts are:

    huggingfastapi
    ├── huggingfastapi   - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for api.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
    │
    tests                  - pytest

      