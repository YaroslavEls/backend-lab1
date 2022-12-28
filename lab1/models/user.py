from lab1.db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    name = db.Column(
        db.String(120), 
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(256),
        unique=False,
        nullable=False
    )
    currency = db.Column(
        db.String(120),
        db.ForeignKey('currency.name'),
        unique=False,
        nullable=False
    )

    entries = db.relationship(
        'EntryModel',
        back_populates='user',
        lazy='dynamic'
    )