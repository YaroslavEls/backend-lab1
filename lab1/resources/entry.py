from datetime import datetime

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from lab1.bl import *
from lab1.db import *
from lab1.schemas import EntrySchema


blp = Blueprint('entry', __name__, description='Operations on entries')

@blp.route('/entry')
class Entry(MethodView):
    @blp.arguments(EntrySchema)
    def post(self):
        req_data = request.get_json()
        if check(req_data['user_id'], USERS) and check(req_data['category_id'], CATEGORIES):
            req_data['id'] = ENTRIES[-1]['id'] + 1
            req_data['date'] = datetime.now()
            ENTRIES.append(req_data)
            return req_data
        abort(400, message='invalid user or category id')

@blp.route('/entries/<int:user_id>')
class EntriesByUser(MethodView):
    def get(self, user_id):
        user_entries = []
        for elem in ENTRIES:
            if elem['user_id'] == int(user_id):
                user_entries.append(elem)
        return user_entries

@blp.route('/entries/<int:user_id>/<int:category_id>')
class EntriesByCategory(MethodView):
    def get(self, user_id, category_id):
        user_entries = []
        for elem in ENTRIES:
            if elem['user_id'] == int(user_id) and elem['category_id'] == int(category_id):
                user_entries.append(elem)
        return user_entries