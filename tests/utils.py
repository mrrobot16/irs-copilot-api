import uuid
from datetime import datetime

# Generate a unique ID
def generate_unique_id(size=20):
    return str(uuid.uuid4())[:size]

# Set current timestamp
def generate_timestamp():
    return datetime.utcnow()

def methods_and_attributes(obj):
    print("Methods of the object:")
    for item in dir(obj):
        if callable(getattr(obj, item)):
            print(item)

# methods_and_attributes = dir(user)

# print("Methods of the object:")
# for item in methods_and_attributes:
#     if callable(getattr(user, item)):
#         print(item)