import uuid
from datetime import datetime
from db.firebase import firestore


# Generate a unique ID
def generate_unique_id(size=20):
    return str(uuid.uuid4())[size]

# Set current timestamp
def generate_timestamp():
    return datetime.utcnow()

def convert_doc_refs(obj):
    count = 0
    """
    Recursively convert DocumentReference objects in a nested data structure to dictionaries.
    """
    if isinstance(obj, firestore.DocumentReference):
        print('count', count)
        count += 1
        # Fetch the actual document data if you want
        # Be aware of read costs and handle errors appropriately
        doc = obj.get()
        if doc.exists:
            doc_data = doc.to_dict()
            # Here, we apply convert_doc_refs recursively on the fetched data
            return convert_doc_refs(doc_data)
        else:
            return None  # Handle non-existing documents as you see fit
        print('count 2', count)
    elif isinstance(obj, list):
        # Handle lists by applying the function recursively to each element
        return [convert_doc_refs(item) for item in obj]
    elif isinstance(obj, dict):
        # Handle dictionaries by applying the function recursively to each value
        return {key: convert_doc_refs(value) for key, value in obj.items()}
    else:
        # For any other type, return the object as is
        return obj
