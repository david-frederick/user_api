from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
	username = fields.Str(required=True, validate=validate.Regexp(r'^[a-zA-Z0-9]+$'))
	first_name = fields.Str(required=True)
	last_name = fields.Str(required=True)
	email = fields.Str(required=True, validate=validate.Email())


class UserUpdateSchema(Schema):
	first_name = fields.Str()
	last_name = fields.Str()
	email = fields.Str(validate=validate.Email())

