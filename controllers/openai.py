from flask import Blueprint, jsonify, request
from services.openai import gpt3_completion, gpt4_completion

# # Create a blueprint instance
openai_controller = Blueprint('openai_controller', __name__)

# Define routes using the blueprint
@openai_controller.route('/')
def health():
    return jsonify({'status': 'ok'})

@openai_controller.route('/chat', methods=['POST'])
def chat():
    prompt = request.get_json()['prompt']
    response = gpt3_completion(prompt)
    return jsonify({'response': response})

@openai_controller.route('/chat-gpt4', methods=['POST'])
def chatgpt4():
    prompt = request.get_json()['prompt']
    response = gpt4_completion(prompt)
    return jsonify({'response': response})

@openai_controller.route('/conversation', methods=['POST'])
def conversation():
    prompt = request.get_json()['prompt']
    response = gpt3_completion(prompt)
    # response = gpt4_completion(prompt)
    return jsonify({'response': response})