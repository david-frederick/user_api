from marshmallow import Schema, fields


class UserSchema(Schema):
	username = fields.Str(required=True)
	first_name = fields.Str(required=True)
	last_name = fields.Str(required=True)
	email = fields.Str(required=True)

class UserUpdateSchema(Schema):
	first_name = fields.Str()
	last_name = fields.Str()
	email = fields.Str()

