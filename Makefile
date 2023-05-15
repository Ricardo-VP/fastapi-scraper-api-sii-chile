override SHELL := /bin/bash

install: # Install the project dependencies
	poetry install

up: # Run the web app
	poetry run uvicorn app.main:app --reload

test: # Run the tests of the app
	poetry run pytest