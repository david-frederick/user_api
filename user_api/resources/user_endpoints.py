from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint, abort
from db import users
from schemas import UserSchema, UserUpdateSchema

UserBlueprint = Blueprint('users', __name__, description='REST API operations on users.')


@UserBlueprint.route('/users/<string:username>')
class UserEndpoints(MethodView):
	@UserBlueprint.response(200, UserSchema)
	def get(self, username: str):
		try:
			return users[username]
		except KeyError:
			abort(404, message='User not found')

	@UserBlueprint.arguments(UserUpdateSchema)
	@UserBlueprint.response(200, UserSchema)
	def put(self, user_data: UserUpdateSchema, username: str):
		try:
			user = users[username]
			user |= user_data
			return user
		except KeyError:
			abort(404, message='User not found')


@UserBlueprint.route('/users')
class UserListEndpoints(MethodView):
	@UserBlueprint.response(200, UserSchema(many=True))
	def get(self):
		try:
			sort = request.args.get('order_by') or 'username'
			if sort in ('username', 'email', 'first_name', 'last_name'):
				return sorted(users.values(), key=lambda x: x[sort])
			abort(404, message='Unknown parameter submitted. Please use `order_by` to sort your data')
		except AttributeError:
			abort(404, message='Users not accessible')

	@UserBlueprint.arguments(UserSchema)
	@UserBlueprint.response(200, UserSchema)
	def post(self, user_data: UserSchema):
		users[user_data['username']] = user_data
		return user_data, 201
