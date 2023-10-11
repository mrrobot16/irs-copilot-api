from flask import Blueprint, jsonify, request
from services.user import get_users, new_user, get_user, update_user    

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@user_controller.route('/', methods=['GET'])
def get_all():
    return jsonify({'status': 200, 'data': get_users()})

@user_controller.route('/<id>', methods=['GET'])
def get(id):
    return jsonify({'status': 200, 'data': get_user(id)})

@user_controller.route('/new', methods=['POST'])
def new():
    email = request.get_json()['email']
    password = request.get_json()['password']
    return jsonify({'status': 200, 'data': new_user(email, password)})

@user_controller.route('/update/<id>', methods=['POST'])
def update(id):
    email = request.get_json()['email']
    # password = request.get_json()['password']
    return jsonify({'status': 200, 'data': update_user(id, email)})
