"""Initialize the Flask application."""

from flask import Flask

from local_rag.app.chat.routes import chat_bp
from local_rag.app.home import home_bp


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object("local_rag.app.config.Config")

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(chat_bp, url_prefix="/chat")
    return app
