from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import users
from schemas import UserSchema

UserBlueprint = Blueprint('users', __name__, description='REST API operations on users.')


@UserBlueprint.route('/users/<string:username>')
class User(MethodView):
	@UserBlueprint.response(200, UserSchema)
	def get(self, username: str):
		try:
			return users[username]
		except KeyError:
			abort(404, message='User not found')
