from flask import Blueprint, current_app, jsonify, request
from langchain_community.llms.ollama import Ollama
from marshmallow import Schema, ValidationError, fields

from local_rag.app.config import LLM_MODEL

# Initialize your Blueprint and Ollama model
chat_bp = Blueprint("chat", __name__)
llm = Ollama(model=LLM_MODEL)


# Define your request schema with Marshmallow
class CompletionSchema(Schema):
    prompt = fields.Str(required=True)
    attachments = fields.Str(required=False)


# Instantiate the schema
completion_schema = CompletionSchema()


@chat_bp.route("/completions", methods=["POST"])
def completions():
    # Validate and deserialize input
    data = completion_schema.load(request.json)

    # Get the completion from Ollama
    response_data = llm(prompt=data.get("prompt"))

    # Send the response
    return jsonify({"status": "success", "message": "POST request received", "data": response_data}), 200


@chat_bp.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    # Return a json with the validation errors
    return jsonify(err.messages), 400
