from user import User
from firebase import firestore_db
from flask import jsonify


"""
created_at
October 9, 2023 at 10:19:04 PM UTC-4
(timestamp)


id
"c3bc7226-abe8-47a6-a"
(string)


messages
(array)


0
/messages/529876c1-89b9-4868-8
(reference)


name
"New conversation id:c3"
(string)


user_id
"e6e86893-59eb-443a-a"
(string)
"""

def convert_to_json_serializable(doc):
    print(str(type(doc)))
    # json = {
    #     'id': doc.id,
    #     'created_at': doc.get('created_at'),
    #     'name': doc.get('name'),
    #     'user_id': doc.get('user_id'),
    #     'messages': doc.get('messages')
    # }
    # return doc.get().to_dict()

def get_all_users():
    user_model = User(firestore_db)
    users = user_model.get_all()
    user = users[0]
    doc = user['conversations'][0]
    print(doc)
    json = convert_to_json_serializable(doc)
    # print(json)
    return users;
    

users = get_all_users()
