from flask import Blueprint, request, jsonify
from .app import (JWTManager, jwt_required, create_access_token,
jwt_refresh_token_required, create_refresh_token,
get_jwt_identity, set_access_cookies,
set_refresh_cookies, unset_jwt_cookies)
from flask_cors import CORS, cross_origin
from api.database.dataBase import Database
import datetime
from api.validation.user_auth import Auth_user

token_expire = datetime.timedelta(days=0.1)

db = Database()

base_url= '/api/v1'

blueprint = Blueprint("user_login", __name__)

CORS(blueprint, supports_credentials=True)

@blueprint.route(base_url + '/auth/login', methods=['POST'])
def login_user_auth():

	user_login = request.get_json()

	query_login = "SELECT username, password, admin from users WHERE username = '{}' and password = '{}' ".format(
		user_login['username'], user_login['password'])

	if not db.query(query_login):
		return jsonify({"error": "invalid credentials"}), 401

	resp = ""
	if db.query(query_login)[0]['admin']:
		resp = jsonify({"message": "Logged in as admin. Dashboard"})
		
	else:
		resp = jsonify({"message": "Logged in successfully. Welcome to sendIT"})
	access_token= create_access_token(identity= user_login['username'], expires_delta=token_expire)
	refresh_token= create_access_token(identity=user_login['username'], expires_delta=token_expire)
	
	
	set_access_cookies(resp, access_token)
	set_refresh_cookies(resp, refresh_token)

	#update headers
	#resp.headers['Acess-Control-Allow-Credentials'] = True
	return resp, 200


@blueprint.route(base_url + '/auth/user', methods=['POST'])
def register_user():

	user_info = request.get_json()

	Auth_user.verify(user_info)

	query_sql = """INSERT INTO USERS (email, password, handphone, username) VALUES (%s,
	%s, %s, %s)"""

	query_check_username = "SELECT * FROM users WHERE username = '{}' ".format(user_info['username'])

	query_info = (user_info['email'], user_info['password'], user_info['handphone'],
	 user_info['username'])
	print(query_info)
	print(db.query(query_check_username))

	if db.query(query_check_username):
		return jsonify({"error": "username Already Exists!"}), 400

	db.insert(query_sql, query_info)

	return jsonify({"Register message": "Succesfully registerd to sendIT"}), 201


@blueprint.route(base_url + '/auth/logout', methods=['GET'])
@jwt_required
def logout_revoke_jwt():
    resp = jsonify({'logout': "Logged out of sendIT"})
    unset_jwt_cookies(resp)
    return resp, 200

@blueprint.route('/')
def homepage():
	return jsonify({"message":"Welcome to sendIT. Pleasure to be of service"}), 200

@blueprint.route(base_url + '/auth/all/users', methods=['GET'])
def get_all_users():
	all_users = """SELECT username FROM users;"""
	users =  db.query(all_users)
	return jsonnify({"users": users}), 200