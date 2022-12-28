from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token

from sqlalchemy.exc import IntegrityError

from passlib.hash import pbkdf2_sha256

from lab1.db import db
from lab1.schemas import UserSchema, RegistrationSchema, LoginSchema, LoginResponseSchema
from lab1.models.user import UserModel


blp = Blueprint('auth', __name__, description='Login and Registration')

@blp.route('/registration')
class Registration(MethodView):
    @blp.arguments(RegistrationSchema)
    @blp.response(200, UserSchema)
    def post(self, req_data):
        req_data['password'] = pbkdf2_sha256.hash(req_data['password'])
        user = UserModel(**req_data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Error while creating new user')
        return user

@blp.route('/login')
class Login(MethodView):
    @blp.arguments(LoginSchema)
    @blp.response(200, LoginResponseSchema)
    def post(self, req_data):
        query = UserModel.query.filter(UserModel.name == req_data['name'])
        user = query.one()

        if user and pbkdf2_sha256.verify(req_data['password'], user.password):
           user.access_token = create_access_token(identity=user.id)  
        else:
            abort(400, message='Wrong user name or password')
        return user
