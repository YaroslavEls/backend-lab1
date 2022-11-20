from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import IntegrityError

from lab1.db import db
from lab1.schemas import EntrySchema
from lab1.models.entry import EntryModel


blp = Blueprint('entry', __name__, description='Operations on entries')

@blp.route('/entry')
class Entry(MethodView):
    @blp.arguments(EntrySchema)
    @blp.response(200, EntrySchema)
    def post(self, req_data):
        entry = EntryModel(**req_data)
        try:
            db.session.add(entry)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Error while creating entry')
        return entry

@blp.route('/entries/<int:user_id>')
class EntriesByUser(MethodView):
    @blp.response(200, EntrySchema(many=True))
    def get(self, user_id):
        query = EntryModel.query.filter(EntryModel.user_id == user_id)
        return query.all()

@blp.route('/entries/<int:user_id>/<int:category_id>')
class EntriesByCategory(MethodView):
    @blp.response(200, EntrySchema(many=True))
    def get(self, user_id, category_id):
        query = EntryModel.query.filter(EntryModel.user_id == user_id)
        query = query.filter(EntryModel.category_id == category_id)
        return query.all()