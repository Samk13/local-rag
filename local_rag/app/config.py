from enum import Enum


class Config:
    DEBUG = True


ALLOWED_EXTENSIONS = {"md", "py", "json", "cfg", "html", "css"}

LLM_MODEL = "mistral-openorca"


class LLMModels(Enum):
    MISTRAL_OPENORCA = "mistral-openorca"
    CLAUDE_3_OPUS_20240229 = "claude-3-opus-20240229"
    GPT4 = "gpt4"
