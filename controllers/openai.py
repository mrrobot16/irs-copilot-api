from flask import Blueprint, jsonify, request
from services.openai import chat_completion
from constants.openai import OPENAI_ENGINE, OPENAI_CHAT_COMPLETION_ENDPOINT_ERROR
from config import OPENAI_API_KEY_DEV
import requests
from decorators import app_enabled_required

# # Create a blueprint instance
openai_controller = Blueprint('openai_controller', __name__)

# Define routes using the blueprint
@openai_controller.route('/health')
@app_enabled_required
def health():
    return jsonify({'status': 'ok'})

@openai_controller.route('/chat-completion', methods=['POST'])
@app_enabled_required
def chat():
    data = request.get_json()
    prompt = data.get('prompt', None)
    engine = data.get('engine', None)
    if prompt is None:
        error = OPENAI_CHAT_COMPLETION_ENDPOINT_ERROR, OPENAI_CHAT_COMPLETION_ENDPOINT_ERROR['status_code']
        return jsonify(error)
    else:
        response = chat_completion(prompt, engine)
        return jsonify({'response': response})

@openai_controller.route('/status', methods=['GET'])
@app_enabled_required
def check_openai_status():

    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY_DEV}',
    }

    response = requests.get('https://api.openai.com/v1/engines', headers=headers)
    
    if response.status_code == 200:
        response = {
            'status': 'success', 
            'message': 'OpenAI API is operational.', 
            'response': response.json()
        }
        return jsonify(response), 200
    else:
        response = {
            "status": 'failure', 
            'message': f'Issue with OpenAI API. Status code: {response.status_code}', 
            'response': response.json()
        }
        return jsonify(response), 500