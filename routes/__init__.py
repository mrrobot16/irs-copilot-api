# register.py

from controllers.openai import openai_controller
from controllers.user import user_controller
from controllers.conversation import conversation_controller
from flask import jsonify
from config import FIREBASE_CREDENTIALS

allowed_origins = ['https://irs-copilot.vercel.app/', 'https://irs-copilot.vercel.app', 'http://localhost:3000']

def register(app):
    print("len(FIREBASE_CREDENTIALS)", len(FIREBASE_CREDENTIALS['private_key']))
    @app.route('/')
    def health():
        return jsonify({'status': 'ok'})

    app.register_blueprint(openai_controller, url_prefix='/openai')
    app.register_blueprint(user_controller, url_prefix='/users')
    app.register_blueprint(conversation_controller, url_prefix='/conversations')

    return app