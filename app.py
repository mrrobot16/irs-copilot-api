import json
from flask import Flask, jsonify, request
import openai

from controllers.openai import openai_controller
from controllers.firebase import firebase_controller
from controllers.user import user_controller
from controllers.conversation import conversation_controller


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    openai_api_key = app.config['OPENAI_API_KEY']
    openai.api_key = openai_api_key

    app.register_blueprint(openai_controller, url_prefix='/openai')
    app.register_blueprint(firebase_controller, url_prefix='/firebase')
    app.register_blueprint(user_controller, url_prefix='/users')
    app.register_blueprint(conversation_controller, url_prefix='/conversations')

    @app.route('/')
    def health():
        return jsonify({'status': 'ok'})

    return app

app = create_app()

if __name__ == "__main__":
    app.run()