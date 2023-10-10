from models import User, Conversation, Message
from firebase import firestore_db, firestore

def create_user():
    user = User(firestore_db)
    return user.create()

def create_conversation(user_id):
    conversation = Conversation(firestore_db)
    return conversation.create(user_id)

def create_message(user_id, conversation_id, content, role):
    message = Message(firestore_db, user_id, conversation_id)
    return message.create(user_id, conversation_id, content, role)

def create_user_conversation_message():
    user = create_user()
    user_id = user.get().to_dict().get('id')
    print('user_id', user_id)

    conversation = create_conversation(user_id)
    conversation_id = conversation.get().to_dict().get('id')
    print('conversation_id', conversation_id)

    content = 'Hello Perkins, what is a 1040?'
    role = 'user'
    message = create_message(user_id, conversation_id, content, role)
    message_id = message.get().to_dict().get('id')
    print('message_id', message_id)

create_user_conversation_message()