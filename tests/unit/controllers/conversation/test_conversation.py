import random

from controllers.conversation import conversation_controller
from tests.fixtures.models.conversation import conversation_fixture

messages = conversation_fixture['messages']
random_message = messages[random.randint(0, len(messages) - 1)]
random_new_message = messages[random.randint(0, len(messages) - 1)]

def test_health(client):
    response = client.get("/conversations/health")
    assert response.status_code == 200

def test_get_all(client):
    response = client.get("/conversations/")
    assert response.status_code == 200

def test_get_all_by_user(client):
    user_id = "0c70f67e-da6a-4c4c-b"
    response = client.get(f"/conversations/user/{user_id}")
    assert response.status_code == 200

def test_get(client):
    conversation_id = "26385545-bb6f-4158-a"
    response = client.get(f"/conversations/{conversation_id}")
    assert response.status_code == 200

def test_new(client):
    user_id = "0c70f67e-da6a-4c4c-b"
    json = {
        "user_id": user_id,
        "message": random_message,
    }
    response = client.post(f"/conversations/new", json=json)
    assert response.status_code == 200

def test_new_message(client):
    id = "26385545-bb6f-4158-a"
    user_id = "0c70f67e-da6a-4c4c-b"
    json = {
        "user_id": user_id,
        "message": random_new_message
    }
    response = client.post(f"/conversations/message/new/{id}", json=json)
    assert response.status_code == 200

def test_update(client):
    conversation_id = "26385545-bb6f-4158-a"
    json = {
        "name": random_new_message,
    }
    response = client.put(f"/conversations/update/{conversation_id}", json=json)
    assert response.status_code == 200


def test_deactivate(client):
    conversation_id = "26385545-bb6f-4158-a"
    response = client.put(f"/conversations/deactivate/{conversation_id}")
    assert response.status_code == 200
