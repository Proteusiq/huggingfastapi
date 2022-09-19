SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

DEFAULT_MODEL_PATH := ./ml_model/

ifeq ($(API_KEY),)
API_KEY := $(python -c "import uuid;print(str(uuid.uuid4()))")
endif


# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

test:
	python -m pip install --upgrade pip && pip install setuptools tox
	tox

install: generate_dot_env
	pip install --upgrade pip && pip install -r requirements.txt

run: 
	- python -c "import subprocess;print(subprocess.run(['hostname','-I'],capture_output=True,text=True).stdout.strip())"
	PYTHONPATH=huggingfastapi/ uvicorn huggingfastapi.main:app --reload --host 0.0.0.0

build: generate_dot_env
	docker compose build

deploy: generate_dot_env
	docker compose build
	docker compose up -d

down:
	docker compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

clean:
	-find . -name '*.pyc' -exec rm -rf {} \;
	-find . -name '__pycache__' -exec rm -rf {} \;
	-find . -name 'Thumbs.db' -exec rm -rf {} \;
	-find . -name '*~' -exec rm -rf {} \;
	-rm -rf .cache
	-rm -rf build
	-rm -rf dist
	-rm -rf *.egg-info
	-rm -rf htmlcov*
	-rm -rf .tox/
	-rm -rf docs/_build
	-rm -r .coverage
	-rm -rf .pytest_cache