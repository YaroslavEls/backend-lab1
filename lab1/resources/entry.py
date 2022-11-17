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
    @blp.response(200, EntrySchema)
    def post(self, req_data):
        if not check(req_data['user_id'], USERS) or not check(req_data['category_id'], CATEGORIES):
            abort(400, message='invalid user or category id')
        req_data['id'] = ENTRIES[-1]['id'] + 1
        req_data['date'] = datetime.now()
        ENTRIES.append(req_data)
        return req_data

@blp.route('/entries/<int:user_id>')
class EntriesByUser(MethodView):
    @blp.response(200, EntrySchema(many=True))
    def get(self, user_id):
        if not check(user_id, USERS):
            abort(400, message='invalid user id')
        user_entries = []
        for elem in ENTRIES:
            if elem['user_id'] == int(user_id):
                user_entries.append(elem)
        return user_entries

@blp.route('/entries/<int:user_id>/<int:category_id>')
class EntriesByCategory(MethodView):
    @blp.response(200, EntrySchema(many=True))
    def get(self, user_id, category_id):
        if not check(user_id, USERS) or not check(category_id, CATEGORIES):
            abort(400, message='invalid user or category id')
        user_entries = []
        for elem in ENTRIES:
            if elem['user_id'] == int(user_id) and elem['category_id'] == int(category_id):
                user_entries.append(elem)
        return user_entries