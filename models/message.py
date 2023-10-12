from utils import generate_timestamp, generate_unique_id
from db.firebase import firestore

class Message:

    def __init__(self, user_id, conversation_id, content, role):
        self.id = generate_unique_id()
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.content = content
        self.role = role
        self.created_at = generate_timestamp()