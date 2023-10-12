from models.conversation import Conversation
from db.firebase import firestore_db, firestore
from utils.firebase import convert_doc_refs

conversation = Conversation(firestore_db)

# def get_conversations():
#     conversations = Conversation(firestore_db)
#     return conversations.get_all()

def new_conversation(user_id, message):
    return conversation.new(user_id, message)

def add_message(user_id, conversation_id, message):
    return conversation.add_message(conversation_id, message)

# def get_coversation(id):
#     conversation = Conversation(firestore_db)
#     return conversation.get(id)

# def update_conversation(id, email, password = None):
#     return conversation.update(id, email, password)

# def delete_conversation(id):
#     return conversation.delete(id)

# def deactivate_conversation(id):
#     return conversation.deactivate(id)