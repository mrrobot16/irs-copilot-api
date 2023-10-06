from flask import Blueprint, jsonify, request
from services.gpt import gpt3_completion, gpt4_completion

# # Create a blueprint instance
gpt = Blueprint('gpt', __name__)

# Define routes using the blueprint
@gpt.route('/')
def health():
    return jsonify({'status': 'ok'})


@gpt.route('/chat', methods=['POST'])
def chat():
    prompt = request.get_json()['prompt']
    response = gpt3_completion(prompt)
    return jsonify({'response': response})

@gpt.route('/chat-gpt4', methods=['POST'])
def chatgpt4():
    prompt = request.get_json()['prompt']
    response = gpt4_completion(prompt)
    return jsonify({'response': response})