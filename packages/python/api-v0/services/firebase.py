import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
credentials = credentials.Certificate("./credentials/firebase/irscopilot-dev-firebase-adminsdk-72ar9-0b73aebc83.json")
firebase_admin.initialize_app(credentials)

# Firestore database instance
firestore_db  = firestore.client()

def query_conversations_by_user_id(user_id):
    user_ref = firestore_db.collection('users').document(user_id)
    conversations_ref = user_ref.collection('conversations')

    conversations_with_messages = []

    for conversation_doc in conversations_ref.stream():
        conversation_data = conversation_doc.to_dict()
        conversation_id = conversation_doc.id
        created_at = conversation_data.get('created_at')  # Assuming 'created_at' is a field in your conversation document
        
        # Get messages for this conversation
        messages_ref = conversations_ref.document(conversation_id).collection('messages')
        messages = []
        for message_doc in messages_ref.stream():
            message_data = message_doc.to_dict()
            messages.append(message_data)
        
        # Add conversation with its messages to the result list
        conversation_with_messages = {
            'conversation_id': conversation_id,
            'created_at': created_at,
            'messages': messages
        }
        
        conversations_with_messages.append(conversation_with_messages)

    # Return data structure with user_id and conversations
    return {
        'user_id': user_id,
        'conversations': conversations_with_messages
    }