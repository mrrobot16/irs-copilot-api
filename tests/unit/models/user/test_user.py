import time
import random

from models.user import User
from tests.fixtures.models.user import user_fixture
from db.firebase import firestore_db
from utils.firebase import convert_doc_refs

user = User(firestore_db)

emails = [
    "h@testng.com",
    "i@testng.com",
    "j@testng.com",
    "k@testng.com",
]

random_email = emails[random.randint(0, len(emails) - 1)]

def test_get_all():
    users = user.get_all()
    assert len(users) > 0

def test_new():
    # print(user)
    new_user = user.new(user_fixture["email"], user_fixture["password"], user_fixture["conversations"])
    new_user = user.get(new_user["id"])
    assert new_user['email'] == "johndoe@example.com"
    assert new_user['conversations'] == []

def test_get():
    id = '0c70f67e-da6a-4c4c-b'
    get_user = user.get(id)
    assert get_user['id'] == id

def test_update():
    id = '0c70f67e-da6a-4c4c-b'
    email = random_email
    user.update(id, email)
    assert user.get(id)['email'] == email

def test_deactivate_user():
    id = '0c70f67e-da6a-4c4c-b'
    user.deactivate(id)
    assert user.get(id)['active'] == False

def test_activate_user():
    time.sleep(3)
    id = '0c70f67e-da6a-4c4c-b'
    user.activate(id)
    assert user.get(id)['active'] == True