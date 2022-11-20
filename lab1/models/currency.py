from lab1.db import db


class CurrencyModel(db.Model):
    __tablename__ = 'currency'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    name = db.Column(
        db.String(120), 
        unique=True, 
        nullable=False
    )

    users = db.relationship(
        'UserModel'
    )
    entries = db.relationship(
        'EntryModel'
    )