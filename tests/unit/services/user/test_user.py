import time
import random

from db.firebase import firestore_db, firestore
from services.user import get_users, new_user, get_user, update_user, delete_user, deactivate_user, activate_user

emails = [
    "h@testng.com",
    "i@testng.com",
    "j@testng.com",
    "k@testng.com",
]

random_email = emails[random.randint(0, len(emails) - 1)]

def test_get_users():
    users = get_users()
    assert len(users) > 0

def test_get_user():
    id = "0c70f67e-da6a-4c4c-b"
    user = get_user(id)
    assert user["id"] == id

def test_new_user():
    email = "testing_new_user_service@testing.com"
    user = new_user("testing_new_user_service@testing.com", None)
    assert user["email"] == "testing_new_user_service@testing.com"

def test_update_user():
    id = "638e98f0-de21-4f24-b"
    email = random_email
    user = update_user(id, email)
    assert user["email"] == email

def test_deactivate_user():
    id = "638e98f0-de21-4f24-b"
    user = deactivate_user(id)
    assert user["active"] == False

def test_activate_user():
    time.sleep(3)
    id = "638e98f0-de21-4f24-b"
    user = activate_user(id)
    assert user["active"] == True

# Not really needing to test this, but it's nice to have.
# def test_delete_user(id):
#     return user.delete(id)