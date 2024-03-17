import sys

from flask import Blueprint, current_app, jsonify, request
from marshmallow import Schema, ValidationError, fields

from local_rag.app.config import LLMModels

from ..models.llm_model import get_llm_response

# Initialize your Blueprint and Ollama model
chat_bp = Blueprint("chat", __name__)


# Define your request schema with Marshmallow
class CompletionSchema(Schema):
    prompt = fields.Str(required=True)
    system = fields.Str(required=True)
    model = fields.Enum(enum=LLMModels, by_value=True, required=True)
    temperature = fields.Float(required=True)


# Instantiate the schema
completion_schema = CompletionSchema()


@chat_bp.route("/completions", methods=["POST"])
def completions():
    # Validate and deserialize input
    data = completion_schema.load(request.json)
    print(data, file=sys.stderr)
    # TODO: sanitize the input

    # Get the completion from Ollama
    response_data = get_llm_response(prompt=data)

    # Send the response
    return jsonify({"status": "success", "data": response_data}), 200


@chat_bp.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    # Return a json with the validation errors
    return jsonify(err.messages), 400
