# Local RAG

Local RAG (retrieval-augmented generation) is a tool that allow you to chat with your repo in a local environment.
you can add your github repo and then chat with it.

## Installation

- To install the Local RAG, you need to have [Ollama](https://ollama.com/download)
TODO setup docker-compose file

- Clone the repository

Install it:

```bash
make install
```

## Usage

Run the Local RAG:

```bash
make run
```

## Development

To run the tests:

```bash
make test
```

To run the linter:
We are using ruff

```bash
make format

```

CSS styling
Tailwind CSS is used for styling. To watch the changes in the CSS file, run:

```bash
make watch
```
