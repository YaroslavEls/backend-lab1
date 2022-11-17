from flask_smorest import Api

from lab1 import app
from lab1.resources.category import blp as CategoryBlueprint
from lab1.resources.entry import blp as EntryBlueprint
from lab1.resources.user import blp as UserBlueprint


app.config["PROPAGATE_EXCEPRIONS"] = True
app.config["API_TITLE"] = "Labs"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(CategoryBlueprint)
api.register_blueprint(EntryBlueprint)
api.register_blueprint(UserBlueprint)