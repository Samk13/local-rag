import pytest
from flask import Flask
from local_rag.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    
    with app.app_context():
        app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
