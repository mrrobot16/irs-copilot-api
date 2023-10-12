
import pytest
from models.user import User
from tests.fixtures.models.user_data import user_data
from db.firebase import firestore_db
from utils import hash_password

def test_create_user():
    user = User(firestore_db)
    user.new(user_data["email"], user_data["password"], user_data["conversations"])
    user = user.new(user_data["email"], user_data["password"], user_data["conversations"])
    assert user['email'] == "johndoe@example.com"
    assert user['conversations'] == []

