from models.conversation import Conversation
from services.openai import chat_completion

from db.firebase import firestore_db, firestore

conversation = Conversation(firestore_db)

def get_conversations():
    conversations = Conversation(firestore_db)
    return conversations.get_all()

def get_conversations_by_user(user_id):
    conversations = Conversation(firestore_db)
    return conversations.get_all_by_user(user_id)

def new_conversation(user_id, message):
    return conversation.new(user_id, message)

def new_message(user_id, conversation_id, message):
    return conversation.new_message(user_id, conversation_id, message)

def new_message_to_openai(user_id, conversation_id, message):
    user_message = conversation.new_message(user_id, conversation_id, message)
    openai_response = chat_completion(user_message['content'])    
    return conversation.new_message(user_id, conversation_id, openai_response['api'])

def get_conversation(id):
    conversation = Conversation(firestore_db)
    return conversation.get(id)

def update_conversation(conversation_id, name):
    return conversation.update(conversation_id, name)

def delete_conversation(id):
    return conversation.delete(id)

def deactivate_conversation(id):
    return conversation.deactivate(id)