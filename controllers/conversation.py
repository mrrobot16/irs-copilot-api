from flask import Blueprint, jsonify, request
from services.conversation import get_conversations, get_conversation, new_conversation, update_conversation, deactivate_conversation, delete_conversation, get_conversations_by_user, new_message

conversation_controller = Blueprint('conversation_', __name__)

@conversation_controller.route('/health', methods=['GET'])
def health():
    response = {
        'status': 'ok'
    }
    return jsonify(response)

@conversation_controller.route('/', methods=['GET'])
def get_all():
    response = {
        'status': 200, 
        'data': get_conversations()
    }
    return jsonify(response)

@conversation_controller.route('/user/<user_id>', methods=['GET'])
def get_all_by_user(user_id):
    response = {
        'status': 200, 
        'data': get_conversations_by_user(user_id)
    
    }
    return jsonify(response)

@conversation_controller.route('/<id>', methods=['GET'])
def get(id):
    response = {
        'status': 200, 
        'data': get_conversation(id)
    }
    return jsonify(response)

@conversation_controller.route('/new', methods=['POST'])
def new():
    user_id = request.get_json()['user_id']
    message = request.get_json()['message']
    response = {
        'status': 200, 
        'data': new_conversation(user_id, message)
    }
    return jsonify(response)

@conversation_controller.route('/message/new/<id>', methods=['POST'])
def new_conversation_message(id):
    user_id = request.get_json()['user_id']
    message = request.get_json()['message']
    response = {
        'status': 200, 
        'data': new_message(user_id, id, message)
    }
    return jsonify(response)

@conversation_controller.route('/update/<id>', methods=['PUT'])
def update(id):
    name = request.get_json()['name']
    response = {
        'status': 200, 
        'data': update_conversation(id, name)
    }
    return jsonify(response)

@conversation_controller.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    response = {
        'status': 200,
        'data': delete_conversation(id)
    }
    return jsonify(response)

@conversation_controller.route('/deactivate/<id>', methods=['PUT'])
def deactivate(id):
    response = {
        'status': 200, 
        'data': deactivate_conversation(id)
    }
    return jsonify(response)

# @conversation_controller.route('/delete/<id>', methods=['DELETE'])
# def delete(id):
#     response = {
#         'status': 200,
#         'data': delete_conversation(id)
#     }
#     return jsonify(response)

