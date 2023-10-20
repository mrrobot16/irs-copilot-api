from flask import Blueprint, jsonify, request
from services.openai import chat_completion
from constants.openai import OPENAI_ENGINE, OPENAI_CHAT_COMPLETION_ENDPOINT_ERROR
from config import OPENAI_API_KEY_DEV
import requests

# # Create a blueprint instance
openai_controller = Blueprint('openai_controller', __name__)

# Define routes using the blueprint
@openai_controller.route('/health')
def health():
    return jsonify({'status': 'ok'})

@openai_controller.route('/chat-completion', methods=['POST'])
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
def check_openai_status():

    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY_DEV}',
    }

    response = requests.get('https://api.openai.com/v1/engines', headers=headers)
    
    if response.status_code == 200:
        return jsonify({"status": "success", "message": "OpenAI API is operational."}), 200
    else:
        return jsonify({"status": "failure", "message": f"Issue with OpenAI API. Status code: {response.status_code}"}), 500
