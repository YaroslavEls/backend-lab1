from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from lab1.db import CATEGORIES


blp = Blueprint('category', __name__, description='Operations on categories')

@blp.route('/category')
class Category(MethodView):
    def post(self):
        req_data = request.get_json()
        req_data['id'] = CATEGORIES[-1]['id'] + 1
        CATEGORIES.append(req_data)
        return req_data

@blp.route('/categories')
class Categories(MethodView):
    def get(self):
        return CATEGORIES