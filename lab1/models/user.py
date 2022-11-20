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

    entries = db.relationship(
        'EntryModel',
        back_populates='user',
        lazy='dynamic'
    )