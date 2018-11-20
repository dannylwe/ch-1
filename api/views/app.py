from flask import Flask, abort, request, jsonify, abort, make_response
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
import datetime
#import uuid
from models.parcel_store import *
from database.dataBase import Database
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
	jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies)

app = Flask(__name__)
cors = CORS(app)
jwt = JWTManager(app)

app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'THANOS-will-RetUrn'
app.config['JWT_TOKEN_LOCATION'] = "cookies"
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.wsgi_app = ProxyFix(app.wsgi_app)

token_expire = datetime.timedelta(days=0.1)

base_url= '/api/v1'

@app.route(base_url + '/parcels', methods=['POST'])
@jwt_required
def hello_world():
	parcel_info = request.get_json()
	current_user = get_jwt_identity()

	db = Database()

	query_sql = """INSERT INTO parcel (nickname, pickup, destination, weight, 
	username) VALUES (%s, %s, %s, %s, %s)"""
	query_info = (parcel_info['nickname'], parcel_info['pickup'], parcel_info['destination'],
	 parcel_info['weight'], current_user)

	db.insert(query_sql, query_info)

	return jsonify({"added parcel": query_info}), 201

@app.route(base_url + '/parcels/<int:id>', methods=['GET'])
def gets_by_id(id):

	if request.method == 'GET':
		if type(id) != int:
			abort(400, 'No string literal allowed')

		result = [prod for prod in parcels if prod['id'] == id]

		if result == []:
			return jsonify({"message": "nothing here"}), 200
		return jsonify({"message": result}), 200


@app.route(base_url + '/users/<int:user_id>/parcels', methods=['GET'])
def get_from_user(user_id):

	result = []

	for users in parcels:
		if users['user_id'] == user_id:
			result.append(users)

	if result == []:
		abort(404, 'No such user')
	return jsonify({"message": result})

@app.route(base_url + '/parcels/<int:id>/cancel', methods=['PUT'])
def cancel_order(id):

	post_parcel = request.get_json()

	error_handler(post_parcel)

	for parcel in parcels:
		if parcel['id'] == id:
			parcel['status'] = "cancelled"
			return jsonify({"cancelled": parcel}), 201
	return jsonify({"message": "Id does not exist"}), 200


@app.route(base_url + '/auth/user', methods=['POST'])
def register_user():

	user_info = request.get_json()
	db = Database()

	# print(user_info['username'])

	query_sql = """INSERT INTO USERS (email, password, handphone, username) VALUES (%s,
	%s, %s, %s)"""

	query_check_username = "SELECT * FROM users WHERE username = '{}' ".format(user_info['username'])

	query_info = (user_info['email'], user_info['password'], user_info['handphone'],
	 user_info['username'])

	if db.query(query_check_username):
		return jsonify({"error": "usename Already Exists!"}), 400

	db.insert(query_sql, query_info)

	return jsonify({"Register message": "Succesfully registerd to sendIT"}), 201

@app.route(base_url + '/auth/login', methods=['POST'])
def login_user_auth():

	user_login = request.get_json()
	db = Database()

	query_login = "SELECT username, password from users WHERE username = '{}' and password = '{}' ".format(
		user_login['username'], user_login['password'])

	if not db.query(query_login):
		return jsonify({"error": "invalid credentials"}), 401

	access_token= create_access_token(identity= user_login['username'])
	refresh_token= create_access_token(identity=user_login['username'])
	resp = jsonify({"message": "Logged in successfully. Welcome to sendIT"})

	set_access_cookies(resp, access_token)
	set_refresh_cookies(resp, refresh_token)

	return resp, 200

@app.route(base_url + '/token/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh_token():
    
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)


    resp = jsonify({'message': 'Refreshed access token. You can now continue using sendIT'})
    set_access_cookies(resp, access_token)
    return resp, 200

@app.route(base_url + '/parcels/<int:parcel_id>/status', methods=['PUT'])
@jwt_required
def parcel_status():
	#admin only
	pass

# @app.route(base_url + 'auth/parcels', methods=['POST'])
# @jwt_required
# def post_parcel_jwt():

# 	parcel_info = request.get_json()
# 	current_user = get_jwt_identity()

# 	db = Database()

# 	query_sql = """INSERT INTO parcel (nickname, pickup, destination, weight, 
# 	username) VALUES (%s,
# 	%s, %s, %s)"""
# 	query_info = (parcel_info['nickname'], parcel_info['pickup'], parcel_info['destination'],
# 	 parcel_info['weight'], current_user)

# 	db.insert(query_sql, query_info)

# 	return jsonify({"added parcel": query_info}), 201

@app.route(base_url + '/parcels/<int:parcel_id>/presentLocation', methods=['PUT'])
@jwt_required
def parcel_present_location():
	#admin only
	pass

@app.route(base_url + '/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
def change_status_by_user():
	#creator only change location
	pass

@app.route(base_url + '/auth/logout', methods=['GET'])
@app.route(base_url + '/logout', methods=['GET'])
def logout_revoke_jwt():
    resp = jsonify({'logout': "Logged out of sendIT"})
    unset_jwt_cookies(resp)
    return resp, 200