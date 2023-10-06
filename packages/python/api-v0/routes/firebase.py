from flask import Blueprint, jsonify, request
from services.firebase import query_conversations_by_user_id

firebase = Blueprint('firebase', __name__)

@firebase.route('/', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@firebase.route('/query_conversations_by_user_id', methods=['POST'])
def chat():
    user_id = request.get_json()['user_id']
    data = query_conversations_by_user_id(user_id)
    return jsonify({'status': 200, 'data': data})