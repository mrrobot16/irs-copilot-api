from flask import Blueprint, jsonify, request
from services.firebase import query_conversations_by_user_id, store_messages_by_conversations_id
from db.firebase import firestore

firebase_controller = Blueprint('firebase_controller', __name__)

@firebase_controller.route('/', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@firebase_controller.route('/query_conversations_by_user_id', methods=['POST'])
def query_conversations_by_user():
    user_id = request.get_json()['user_id']
    data = query_conversations_by_user_id(user_id)
    return jsonify({'status': 200, 'data': data})

@firebase_controller.route('/store_conversations_by_user_id', methods=['POST'])
def store_messages_by_conversations():
    user_id = request.get_json()['user_id']
    conversation_id = request.get_json()['conversation_id']
    message_data = request.get_json()['message_data']
    data = store_messages_by_conversations_id(user_id, conversation_id, message_data)
    return jsonify({'status': 200, 'data': data})
