from sqlalchemy.sql import func

from lab1.db import db


class EntryModel(db.Model):
    __tablename__ = 'entry'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        unique=False,
        nullable=False
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        unique=False,
        nullable=False
    )
    created_at = db.Column(
        db.TIMESTAMP,
        server_default=func.now()
    )
    sum = db.Column(
        db.Float(precision=2),
        unique=False,
        nullable=False
    )
    currency = db.Column(
        db.String(120),
        db.ForeignKey('currency.name'),
        unique=False,
        nullable=True
    )

    user = db.relationship(
        'UserModel', 
        back_populates='entries'
    )
    category = db.relationship(
        'CategoryModel', 
        back_populates='entries'
    )