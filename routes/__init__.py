from flask import jsonify, request

from controllers.openai import openai_controller
from controllers.user import user_controller
from controllers.conversation import conversation_controller
from config import APP_ENV

allowed_origins = []
# allowed_origins = ['https://irs-copilot.vercel.app/', 'https://irs-copilot.vercel.app', 'http://localhost:3000']

if APP_ENV == 'production':
    allowed_origins = ['https://irs-copilot.vercel.app/', 'https://irs-copilot.vercel.app']
elif APP_ENV == 'development':
    allowed_origins = ['http://localhost:3000']

def register(app):
    @app.route('/')
    def health():
        return jsonify({'status': 'ok'})

    app.register_blueprint(openai_controller, url_prefix='/openai')
    app.register_blueprint(user_controller, url_prefix='/users')
    app.register_blueprint(conversation_controller, url_prefix='/conversations')

    return app