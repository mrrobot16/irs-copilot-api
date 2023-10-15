from flask import Blueprint, jsonify, request
# from services.openai import gpt3_completion, gpt4_completion
from services.openai import chat_completion

# # Create a blueprint instance
openai_controller = Blueprint('openai_controller', __name__)

# Define routes using the blueprint
@openai_controller.route('/')
def health():
    return jsonify({'status': 'ok'})

@openai_controller.route('/chat-completion', methods=['POST'])
def chat():
    prompt = request.get_json()['prompt']
    response = chat_completion(prompt)
    return jsonify({'response': response})