from datetime import datetime
from db.firebase import firestore_db

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

# Need to now write code that writes conversations from gpt3 prompts and responses.
def store_messages_by_conversations_id(user_id, conversation_id, message_data):

    user_ref = firestore_db.collection('users').document(user_id)
    conversation_ref = user_ref.collection('conversations').document(conversation_id)

    # Construct the message dictionary
    message_id = "message_data.get('id')"
    message = {
        'id': message_id,
        'text': message_data,
        'type': 'user',
        'created_at': datetime.utcnow()
    }

    # Add the message to the conversation
    conversation_ref.collection('messages').document(message_id).set(message)
    return message