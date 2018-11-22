from flask import jsonify, abort
import re

class Auth_user:

	def verify(payload):

		users_info = payload
		# psw_stmt = re.compile(r'[a-zA-Z0-9!@#$%^&*()_+-=]+')
		psw_stmt = re.compile(r'(^[a-zA-Z0-9]+$)')
		email_stmt = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

		if not isinstance(users_info['username'], str) or not isinstance(users_info['email'], str) \
		or not isinstance(users_info['password'], str):
			return jsonify({"error":"username, password and email must be strings"})

		if len(str(users_info['email'])) < 7:
			abort(400, "email too short")

		if len(str(users_info['password'])) < 8:
			abort(400, "password too short")

		if not email_stmt.match(users_info['email']):
			abort(400, "enter a valid email")

		if not psw_stmt.match(users_info['password']):
			abort(400, "not a valid password")

		if not isinstance(users_info['handphone'], int):
			abort(400, "handphone must be an integer")

		if (len(users_info['username']) or len(users_info['email']) or len(users_info['password'])) > 30:
			abort(400, "email/password/username must be < 29")

		if len(str(users_info['handphone'])) > 13:
			abort(400, "please enter valid phone number")

		return



