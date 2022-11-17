from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from lab1.db import CATEGORIES
from lab1.schemas import CategorySchema


blp = Blueprint('category', __name__, description='Operations on categories')

@blp.route('/category')
class Category(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self):
        req_data = request.get_json()
        req_data['id'] = CATEGORIES[-1]['id'] + 1
        CATEGORIES.append(req_data)
        return req_data

@blp.route('/categories')
class Categories(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CATEGORIES