from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    sum = fields.Float(required=True)
    currency = fields.Str(required=False)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    currency = fields.Str(required=True)

class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)