from flask import Blueprint

Users = Blueprint('Users', __name__)

@Users.route('/')
def users():
    return "Users"

# more routes here...