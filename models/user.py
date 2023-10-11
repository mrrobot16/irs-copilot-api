from utils import generate_timestamp, generate_unique_id, hash_password, verify_hashed_password
from models.conversation import Conversation
import warnings

class User:

    def __init__(self, db):
        self.db = db # Reference to the Firestore database
        self.collection_ref = self.db.collection('users') # Reference to the 'users' collection
        self.id = None # string
        self.created_at = None # timestamp
        self.conversations = None # array of conversation reference
        self.email = None # string
        self.password = None # string
    
    def get_all(self):
        users = self.collection_ref.stream()

        # Convert each DocumentSnapshot to a dictionary and add it to a list
        user_list = [user.to_dict() for user in users]
        return user_list

    def get(self, id):
        user_ref = self.collection_ref.document(id)
        user = user_ref.get()
        return user.to_dict() # return user object versus firebase user reference to reduce the amount of reads/writes.
    
    def new(self, email = None, password = None, conversations = []):
        self.id = generate_unique_id()  # Generate a unique 20-character ID
        print(self.id)
        self.created_at = generate_timestamp()  # Get current timestamp
        self.email = email
        self.password = hash_password(email) # NOTE: This is a placeholder for now.
        self.conversations = conversations  # Initialize with an empty array of conversation references

        user = {
            'id': self.id,
            'created_at': self.created_at,
            'email': self.email,
            'conversations': self.conversations,
            'password': str(self.password)
        }

        # Add the user to the 'users' collection
        user_ref = self.collection_ref.document(self.id)
        user_ref.set(user)
        return user # return user object versus firebase user reference to reduce the amount of reads/writes.
    
    def get_by_id(self, id):
        # Suppress "Prefer using the 'filter' keyword argument instead." warning. 
        # This happens when using collection_ref.where()
        warnings.filterwarnings("ignore", category=UserWarning, message="Detected filter using positional arguments. Prefer using the 'filter' keyword argument instead.")

        # Query the collection where 'id' is equal to user_id
        users = self.collection_ref.where('id', '==', id).limit(1).stream()

        # Users is an iterator of DocumentSnapshot
        # Converting DocumentSnapshot to a dictionary
        
        user_list = [user.to_dict() for user in users]
        # NOTE: collection_ref.where returns an array of documents. 
        # We only want the first document in the array.
        return user_list[0]