import uuid
from datetime import datetime
from firebase import firestore
from utils import generate_unique_id, generate_timestamp

class User:

    def __init__(self, db):
        self.db = db
        self.collection_ref = self.db.collection('users')

    def create(self, email = 'black_email@blank.com', conversations = []):
        self.user_id = generate_unique_id()  # Generate a unique 20-character ID
        self.created_at = generate_timestamp()  # Get current timestamp
        self.conversations = conversations  # Initialize with an empty array of conversation references
        self.email = email
        user = {
            'id': self.user_id,
            'created_at': self.created_at,
            'email': self.email,
            'conversations': self.conversations
        }
        
        user_ref = self.collection_ref.document(self.user_id)
        user_ref.set(user)
        # return user_ref
        return self.user_id
    
    def update(self, id, email):
        self.id = id
        self.email = email
        self.updated_at = generate_timestamp()
        user = {
            'id': self.id,
            'email': self.email,
            'updated_at': self.updated_at
        }
        # Here, you can use the set method with merge=True to update or create if the document doesn't exist
        users_ref = self.collection_ref.document(self.id)
        users_ref.set(user, merge=True)
        return user
class Conversation:

    def __init__(self, db):
        self.db = db
        self.collection_ref = self.db.collection('conversations')
        self.user_collection_ref = self.db.collection('users')

    def create(self, user_id, messages = []):
        # NOTE: 
        # This will change based on the context of the conversation.
        self.id = generate_unique_id()
        self.created_at = generate_timestamp()
        self.name = f'New conversation id:{self.id[0:2]}'
        self.user_id = user_id
        self.messages = messages

        conversation = {
            'name': self.name,
            'id': self.id,
            'created_at': self.created_at,
            'messages': self.messages,
            'user_id': self.user_id
        }
        
        conversation_ref = self.collection_ref.document(self.id)
        conversation_ref.set(conversation)

        user_ref = self.user_collection_ref.document(self.user_id)
        user_ref.update({
        'conversations': firestore.ArrayUnion([conversation_ref])
        })

        # return conversation_ref
        return self.id

class Message:

    def __init__(self, db, user_id, conversation_id):
        self.db = db
        self.collection_ref = self.db.collection('messages')


    def create(self, user_id, conversation_id, content, role):

        self.id = generate_unique_id()
        self.created_at = generate_timestamp()
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.content = content
        self.role = role

        message = {
            'id': self.id,
            'user_id': self.user_id,
            'conversation_id': self.conversation_id,
            'created_at': self.created_at,
            'content': self.content,
            'role': self.role # role can only be 'system', 'assistant' or 'user' 
        }

        message_ref = self.collection_ref.document(self.id)
        message_ref.set(message)

        conversation_ref = self.db.collection('conversations').document(self.conversation_id)
        conversation_ref.update({
            'messages': firestore.ArrayUnion([message_ref])
        })

        # return message_ref
        return self.id