.PHONY: help install format

help:
	@echo "Available commands:"
	@echo "install   - Install the package in editable mode"
	@echo "format    - Format the code with isort and black"
	@echo "run       - Run the local RAG server"
	@echo "watch     - Watch the tailwindcss input file and compile it to the output file"
	@echo "test     - test the package"

install:
	pip install -e ".[tests]"

format:
	ruff check --fix && ruff format

watch:
	npx tailwindcss -i ./local_rag/app/static/src/input.css -o ./local_rag/app/static/css/main.css --watch

run:
	python local_rag/run.py

test:
	pytest

default: help