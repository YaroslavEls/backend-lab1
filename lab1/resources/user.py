from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import IntegrityError

from lab1.db import db
from lab1.schemas import UserSchema
from lab1.models.user import UserModel


blp = Blueprint('user', __name__, description='Operations on user')

@blp.route('/user')
class User(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, req_data):
        user = UserModel(**req_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message='User with such name already exists')
        return user

    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()