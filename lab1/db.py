from datetime import datetime

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