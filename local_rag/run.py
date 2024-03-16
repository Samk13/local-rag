"""Main module."""

import os

from dotenv import load_dotenv

from local_rag.app import create_app

# Load environment variables
load_dotenv()

# Create the application instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


# from langchain_community.llms import Ollama
# def start():
#     """Main entry point for the application."""
#     llm = Ollama(model="mistral-openorca")
#     x = llm.invoke("Tell me a joke")
#     print(x)
# secret_key = os.getenv('SECRET_KEY')
