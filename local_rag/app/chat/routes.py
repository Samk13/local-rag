from flask import Blueprint, jsonify, request

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/completions", methods=["GET", "POST"])
def completions():
    if request.method == "POST":
        data = request.json
        return (
            jsonify({"status": "success", "message": "POST request received", "data": data}),
            200,
        )
    else:
        return jsonify({"status": "success", "message": "GET request received"}), 200
