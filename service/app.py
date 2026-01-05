import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "devops-lab")
APP_ENV = os.getenv("APP_ENV", "local")
APP_PORT = int(os.getenv("APP_PORT", 5000))

@app.route("/")
def home():
    return jsonify({
        "app": APP_NAME,
        "environment": APP_ENV,
        "port": APP_PORT
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)

