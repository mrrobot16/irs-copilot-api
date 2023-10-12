from models.conversation import Conversation
from db.firebase import firestore_db

conversation = Conversation(firestore_db)

def new_message(user_id, conversation_id, message):
    return conversation.new_message(user_id, conversation_id, message)
