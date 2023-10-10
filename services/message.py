from models.message import Message
from db.firebase import firestore_db

def create_message(user_id, conversation_id, content, role):
    message = Message(firestore_db, user_id, conversation_id)
    return message.create(user_id, conversation_id, content, role)
