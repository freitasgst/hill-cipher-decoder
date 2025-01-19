# venv settings
export PROJECT_PATH := src
export PYTHONPATH   := $(PROJECT_PATH):tests/fixtures
export VIRTUALENV   := $(PWD)/.venv
export PATH         := $(VIRTUALENV)/bin:$(PATH)

# fix make <= 3.81 (macOS and old Linux distros)
ifeq ($(filter undefine,$(value .FEATURES)),)
SHELL = env PATH="$(PATH)" /bin/bash
endif

all:

.PHONY: .venv

.env:
	echo 'PYTHONPATH="$(PYTHONPATH)"' > .env

.venv:
	python3 -m venv $(VIRTUALENV)
	pip install --upgrade pip

install:
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

install-dev: .venv .env install
	if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

test:
	coverage run --source=$(PROJECT_PATH) --omit=dependencies -m unittest

coverage: test .coverage
	coverage report -m --fail-under=90

lint:
	ruff check --line-length=100 --target-version=py312 .

format:
	ruff format --line-length=100 --target-version=py312 .
