from hmac import compare_digest
from models.user import UserModel


def authenticate(username, password):

    user = UserModel.find_by_username(username)
    if user and compare_digest(password, user.password):
        return user

def identity(payload):
    user_id = 