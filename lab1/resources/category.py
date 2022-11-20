from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import IntegrityError

from lab1.db import db
from lab1.schemas import CategorySchema
from lab1.models.category import CategoryModel


blp = Blueprint('category', __name__, description='Operations on categories')

@blp.route('/category')
class Category(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, req_data):
        category = CategoryModel(**req_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Category with such name already exists')
        return category

@blp.route('/categories')
class Categories(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()