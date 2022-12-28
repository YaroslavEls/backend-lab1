from flask.views import MethodView
from flask_smorest import Blueprint

from lab1.schemas import UserSchema
from lab1.models.user import UserModel


blp = Blueprint('user', __name__, description='Operations on user')

@blp.route('/user')
class User(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()