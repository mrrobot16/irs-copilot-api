from flask import jsonify, request

from controllers.openai import openai_controller
from controllers.user import user_controller
from controllers.conversation import conversation_controller
from config import APP_ENV
from decorators import app_enabled_required

allowed_origins = []
# allowed_origins = ['https://irs-copilot.vercel.app/', 'https://irs-copilot.vercel.app', 'http://localhost:3000']

if APP_ENV == 'production':
    allowed_origins = ['https://irs-copilot.vercel.app/', 'https://irs-copilot.vercel.app']
elif APP_ENV == 'development':
    allowed_origins = ['http://localhost:3000']

def register(app):
    @app.route('/')
    def health():
        try:
            return jsonify({'status': 'ok'}), 200
        except Exception as error:
            error_info = {
                'error_type': type(error).__name__,
                'error_message': str(error)
            }
            return jsonify({'status': error_info}), 500
    
    @app.route('/app_is_enabled')
    @app_enabled_required
    def app_is_enabled():
        try:
            return jsonify({
                'status': 'ok',
                'app_is_enabled': True
            })
        except Exception as error:
            error_info = {
                'error_type': type(error).__name__,
                'error_message': str(error),
                'app_is_enabled': False
            }
            return jsonify({'status': error_info}), 500
    
    
    app.register_blueprint(openai_controller, url_prefix='/openai')
    app.register_blueprint(user_controller, url_prefix='/users')
    app.register_blueprint(conversation_controller, url_prefix='/conversations')

    return app