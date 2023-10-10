from flask import Blueprint, jsonify, request
from services.user import get_all_users, create_user

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@user_controller.route('/get_all', methods=['GET'])
def get_all():
    return jsonify({'status': 200, 'data': get_all_users()})

@user_controller.route('/create', methods=['POST'])
def create():
    # email = request.get_json()['email']
    return jsonify({'status': 200, 'data': create_user()})
