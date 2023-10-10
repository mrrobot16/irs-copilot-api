from utils import generate_timestamp, generate_unique_id
from db.firebase import firestore

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

        return conversation_ref
