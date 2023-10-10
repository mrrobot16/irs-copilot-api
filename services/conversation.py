from db.firebase import firestore_db
from models.conversation import Conversation

def create_conversation(user_id):
    conversation = Conversation(firestore_db)
    return conversation.create(user_id)
