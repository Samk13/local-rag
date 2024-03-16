.PHONY: help install format

help:
	@echo "Available commands:"
	@echo "install   - Install the package in editable mode"
	@echo "format    - Format the code with isort and black"

install:
	pip install -e ".[tests]"

format:
	ruff check --fix && ruff format

default: help