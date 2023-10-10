from models.user import User
from db.firebase import firestore_db, firestore
from utils import convert_doc_refs

def create_user():
    user = User(firestore_db)
    return user.create()

def get_all_users():
    user = User(firestore_db)
    users = user.get_all()
    return convert_doc_refs(users)