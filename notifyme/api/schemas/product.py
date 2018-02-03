from marshmallow import fields, Schema, validate

class ProductSchema(Schema):
    productId = fields.String(required=True)
    url = fields.String(required=True)
    price = fields.Float(required=True) # TODO: change it
    reason = fields.String(required=True)

