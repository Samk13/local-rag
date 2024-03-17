import pytest
from local_rag.app.config import LLMModels
from local_rag.app.models.llm_model import get_llm_response
from unittest.mock import patch, MagicMock


def test_get_completions(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"<title>Welcome to Local RAG</title>" in response.data


def test_get_completions(client):
    response = client.get("/chat/completions")
    assert response.status_code == 405
    assert b"Method Not Allowed" in response.data
