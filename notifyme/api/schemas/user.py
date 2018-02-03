from marshmallow import fields, Schema, validate


class UserSchema(Schema):
    user_id = fields.UUID(required=True)
    name = fields.String(required=True)
