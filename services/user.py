from models.user import User
from db.firebase import firestore_db, firestore
from utils.firebase import convert_doc_refs

user = User(firestore_db)

def get_users():
    users = user.get_all()
    return convert_doc_refs(users)

def new_user(email, password = None):
    return user.new(email)

def get_user(id):
    user_by_id = user.get_by_id(id)
    return convert_doc_refs(user_by_id)