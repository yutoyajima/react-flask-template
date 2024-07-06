from flask import Flask, jsonify

app = Flask(__name__)

# Firebase Admin SDKの初期化

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})