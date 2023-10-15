from flask import Flask, jsonify
import openai
from flask_cors import CORS

from routes import register

def create_app(config_name='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_name)
    CORS(app, origins=["http://localhost:3000"])
    return register(app)


app = create_app()

if __name__ == "__main__":
    app.run()