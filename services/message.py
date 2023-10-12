from models.conversation import Conversation
from db.firebase import firestore_db, firestore
from utils.firebase import convert_doc_refs

conversation = Conversation(firestore_db)

def new_message(user_id, conversation_id, message):
    return conversation.new_message(user_id, conversation_id, message)
