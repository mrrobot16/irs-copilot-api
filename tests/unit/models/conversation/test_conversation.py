import random

from models.conversation import Conversation
from db.firebase import firestore_db
from tests.fixtures.models.conversation import conversation_fixture

conversation = Conversation(firestore_db)

messages = conversation_fixture['messages']

random_message = messages[random.randint(0, len(messages) - 1)]
random_new_message = messages[random.randint(0, len(messages) - 1)]

def test_get_all():
    conversations = conversation.get_all()
    assert len(conversations) > 0

def test_get_all_by_user():
    user_id = "0c70f67e-da6a-4c4c-b"
    get_conversation = conversation.get_all_by_user(user_id)
    assert len(get_conversation) > 0

def test_get():
    id = '26385545-bb6f-4158-a'
    get_conversation = conversation.get(id)
    assert get_conversation['id'] == id

def test_new():
    user_id = "0c70f67e-da6a-4c4c-b"
    message = random_message
    new_conversation = conversation.new(user_id, message)
    assert new_conversation['user_id'] == user_id
    assert new_conversation['messages'][0]['content'] == message['content']
    assert new_conversation['messages'][0]['role'] == message['role']


def test_new_message():
    user_id = "0c70f67e-da6a-4c4c-b"
    conversation_id = "26385545-bb6f-4158-a"
    message = random_new_message
    new_message = conversation.new_message(user_id, conversation_id, message)
    get_conversation = conversation.get(conversation_id)
    assert new_message['user_id'] == user_id
    assert new_message['conversation_id'] == conversation_id
    assert new_message['content'] == message['content']
    assert new_message['role'] == message['role']

def test_update():
    id = '26385545-bb6f-4158-a'
    conversation.update(id, "New Conversation name")
    assert conversation.get(id)['name'] == "New Conversation name"

def test_deactivate():
    id = '26385545-bb6f-4158-a'
    conversation.deactivate(id)
    assert conversation.get(id)['active'] == False

