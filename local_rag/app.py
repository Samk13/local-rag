
"""Main module."""
from langchain_community.llms import Ollama



def start():
    """Main entry point for the application."""
    llm = Ollama(model="mistral-openorca")
    x = llm.invoke("Tell me a joke")
    print(x)



if __name__ == "__main__":
    start()
