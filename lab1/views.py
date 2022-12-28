import os

from flask import jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from lab1 import app
from lab1.db import db
from lab1.resources.category import blp as CategoryBlueprint
from lab1.resources.entry import blp as EntryBlueprint
from lab1.resources.user import blp as UserBlueprint
from lab1.resources.currency import blp as CurrencyBlueprint
from lab1.resources.auth import blp as AuthBlueprint


app.config["PROPAGATE_EXCEPRIONS"] = True
app.config["API_TITLE"] = "Labs"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

db.init_app(app)

api = Api(app)

with app.app_context():
    db.create_all()

api.register_blueprint(CategoryBlueprint)
api.register_blueprint(EntryBlueprint)
api.register_blueprint(UserBlueprint)
api.register_blueprint(CurrencyBlueprint)
api.register_blueprint(AuthBlueprint)

jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({
            "message": "The token has expired.", 
            "error": "token_expired"
        }), 401
    )
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify({
            "message": "Signature verification failed.", 
            "error": "invalid_token", 
            "details": error
        }), 401
    )
@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify({
            "description": "Request does not contain an access token.",
            "error": "authorization_required",
            "details": error
        }), 401
    )