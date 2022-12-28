import os

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

jwt = JWTManager(app)

with app.app_context():
    db.create_all()

api.register_blueprint(CategoryBlueprint)
api.register_blueprint(EntryBlueprint)
api.register_blueprint(UserBlueprint)
api.register_blueprint(CurrencyBlueprint)
api.register_blueprint(AuthBlueprint)