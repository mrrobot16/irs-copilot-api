import pytest
from controllers.user import user_controller
# from tests.fixtures.models import user_data

def test_health(client):
    response = client.get("/users/health")
    assert response.status_code == 200

def test_get_all(client):
    response = client.get("/users/")
    assert response.status_code == 200

def test_get(client):
    user_id = "8643a936-3a4e-454b-a"
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

def test_new(client):
    json = {
        "name": "test_name",
        "email": "test_new_user@testmail.com",
        "password": "test_password"
    }
    response = client.post("/users/new", json=json)
    assert response.status_code == 200

def test_update(client):
    user_id = "8643a936-3a4e-454b-a"
    json = {
        "email": "update_email@testemail.com",
    }
    response = client.put(f"/users/update/{user_id}", json=json)
    assert response.status_code == 200

def test_deactivate(client):
    user_id = "8643a936-3a4e-454b-a"
    response = client.put(f"/users/deactivate/{user_id}")
    assert response.status_code == 200