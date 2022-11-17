from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from lab1.db import USERS
from lab1.schemas import UserSchema


blp = Blueprint('user', __name__, description='Operations on user')

@blp.route('/user')
class User(MethodView):
    @blp.arguments(UserSchema)
    def post(self, req_data):
        req_data['id'] = USERS[-1]['id'] + 1
        USERS.append(req_data)
        return req_data

    def get(self):
        return USERS