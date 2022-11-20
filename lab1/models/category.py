from lab1.db import db


class CategoryModel(db.Model):
    __tablename__ = 'category'

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
        back_populates='category',
        lazy='dynamic'
    )