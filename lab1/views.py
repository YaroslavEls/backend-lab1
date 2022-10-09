from datetime import datetime
from flask import jsonify, request
from lab1 import app


USERS = [
    {
        'id': 1,
        'name': 'John'
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': 'groceries'
    }
]

ENTRIES = [
    {
        'id': 1,
        'user_id': 1,
        'category_id': 1,
        'date': datetime.now(),
        'sum': 150
    }
]


def check_user(id):
    for elem in USERS:
        if elem['id'] == id:
            return True
    return False

def check_category(id):
    for elem in CATEGORIES:
        if elem['id'] == id:
            return True
    return False


@app.post('/user')
def create_user():
    req_data = request.get_json()
    req_data['id'] = USERS[-1]['id'] + 1
    USERS.append(req_data)
    return 'user created successfully'

@app.post('/category')
def create_category():
    req_data = request.get_json()
    req_data['id'] = CATEGORIES[-1]['id'] + 1
    CATEGORIES.append(req_data)
    return 'category created successfully'

@app.post('/entry')
def create_entry():
    req_data = request.get_json()
    if check_user(req_data['user_id']) and check_category(req_data['category_id']):
        req_data['id'] = ENTRIES[-1]['id'] + 1
        req_data['date'] = datetime.now()
        ENTRIES.append(req_data)
        return 'entry added successfully'
    return 'invalid user or category id'

@app.get('/categories')
def get_categories():
    return jsonify({'catrgories': CATEGORIES})

@app.get('/entries/<user_id>')
def get_entries(user_id):
    user_entries = []
    for elem in ENTRIES:
        if elem['user_id'] == int(user_id):
            user_entries.append(elem)
    return jsonify({'entries': user_entries})

@app.get('/entries/<user_id>/<category_id>')
def get_entries_by_category(user_id, category_id):
    user_entries = []
    for elem in ENTRIES:
        if elem['user_id'] == int(user_id) and elem['category_id'] == int(category_id):
            user_entries.append(elem)
    return jsonify({'entries': user_entries})