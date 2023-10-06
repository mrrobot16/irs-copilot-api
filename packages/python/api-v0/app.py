import json
from flask import Flask, jsonify, request
import openai

from routes.gpt import gpt
from routes.firebase import firebase

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    openai_api_key = app.config['OPENAI_API_KEY']
    openai.api_key = openai_api_key

    app.register_blueprint(gpt, url_prefix='/gpt')
    app.register_blueprint(firebase, url_prefix='/firebase')

    @app.route('/')
    def health():
        return jsonify({'status': 'ok'})

    return app

app = create_app()

if __name__ == "__main__":
    app.run()