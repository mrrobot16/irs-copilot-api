from utils import generate_timestamp, generate_unique_id
from db.firebase import firestore
from models.message import Message
class Conversation:

    def __init__(self, db, convesation_id = None):
        self.db = db
        self.collection_ref = self.db.collection('conversations')
        self.user_collection_ref = self.db.collection('users')
        self.messages = [] # Array of Messages
        self.created_at = None # timestamp
        self.updated_at = None # timestamp

    def new(self, user_id, message):
        self.id = generate_unique_id()
        # NOTE: User id of the user who created the conversation.
        self.user_id = user_id 
        # NOTE: This will change based on the context of the conversation.
        self.name = f'Conversation #:{self.id[0:2]}'
        self.created_at = generate_timestamp()
        self.updated_at = self.created_at

        # NOTE: Upon creation we need add first message(message type is 'user') which will be a Message model
        message = Message(self.user_id, self.id, message['content'], message['role'])
        message = {
            'id': message.id,
            'user_id': message.user_id,
            'conversation_id': message.conversation_id,
            'content': message.content,
            'role': message.role,
            'created_at': message.created_at
        }
        self.messages.append(message)

        conversation = {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'messages': self.messages,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

        conversation_ref = self.collection_ref.document(self.id)
        conversation_ref.set(conversation)

        user_ref = self.user_collection_ref.document(self.user_id)
        user_ref.update({
        'conversations': firestore.ArrayUnion([conversation_ref])
        })

        return conversation

    def new_message(self, user_id, conversation_id, message):
        message = Message(user_id, conversation_id, message['content'], message['role'])
        message = {
            'id': message.id,
            'user_id': message.user_id,
            'conversation_id': message.conversation_id,
            'content': message.content,
            'role': message.role,
            'created_at': message.created_at
        }

        conversation_ref = self.collection_ref.document(message['conversation_id'])
        conversation_ref.update({
            'messages': firestore.ArrayUnion([message])
        })

        conversation_ref.update({
            'updated_at': generate_timestamp()
        })

        return message


    # def get_all(self, user_id):
    #     conversations = self.collection_ref.stream()
    #     conversations_list = []
    #     for conversation in conversations:
    #         conversations_list.append(conversation.to_dict())
    #     return conversations_list
    
    # def get(self, id):
    #     conversation_ref = self.collection_ref.document(id)
    #     conversation = conversation_ref.get().to_dict()
    #     return conversation