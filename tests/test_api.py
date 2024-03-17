import pytest


def test_get_completions(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"<title>Welcome to Local RAG</title>" in response.data


def test_get_completions(client):
    response = client.get("/chat/completions")
    assert response.status_code == 200
    assert response.json['status'] == 'success'
