from langchain_community.llms.ollama import Ollama


def get_llm_response(prompt=None):
    llm_instance = Ollama(
        model=prompt.get("model").value, system=prompt.get("system"), temperature=prompt.get("temperature")
    )
    response = llm_instance(prompt=prompt.get("prompt"))
    return response
