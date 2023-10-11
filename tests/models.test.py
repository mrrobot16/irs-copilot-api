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

def update_user(id, email):
    user = User(firestore_db)
    return user.update(id, email)

# user = create_user()
# # user_id = user.get().to_dict().get('id')
# user_id = user
# print('user_id', user_id)

# conversation = create_conversation(user_id)
# # conversation_id = conversation.get().to_dict().get('id')
# conversation_id = conversation
# print('conversation_id', conversation_id)

# content = 'Hello Jarvies, what is a 1099?'
# role = 'user'
# message = create_message(user_id, conversation_id, content, role)
# # message_id = message.get().to_dict().get('id')
# message_id = message
# print('message_id', message_id)

user_id = 'b51ccb22-ed74-4bd2-8'
email = 'hector@gmail.com'
user = update_user(user_id, email)
print('updated_user', user)



