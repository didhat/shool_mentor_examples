from flask import Flask, request
from flask_pydantic import validate
from pydantic import ValidationError

from src.validators import InputFullName

app = Flask(__name__)


@app.route("/hello")
def hello():
    return {"data": {"res": "Hello, world!"}}, 201


@app.route("/hello/<string:name>")
def hello_name(name):
    return {"data": {"res": f"Hello {name}"}}


@app.route("/hello", methods=["POST"])
def hello_post():
    params = request.json
    try:
        user_data = InputFullName(**params)
    except ValidationError:
        return {"error": "ValidationError"}, 401

    return {"data": {
        "res": f"Hello {user_data.name} {user_data.surname}"
    }}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
