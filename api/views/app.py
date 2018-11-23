from flask import Flask, abort, request, jsonify, abort, make_response
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
import datetime
#import uuid remove unused
from api.models.parcel_store import *
from api.database.dataBase import Database
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
	jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies)
from api.validation.parcel_validation import Verify
from api.validation.user_auth import Auth_user
from api.views import cred_auth_users

app = Flask(__name__)
db = Database()
db.create_table()
app.register_blueprint(cred_auth_users.blueprint)

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
def post_single_parcel():
	parcel_info = request.get_json()
	current_user = get_jwt_identity()

	Verify.error_handler(parcel_info)

	query_sql = """INSERT INTO parcel (nickname, pickup, destination, weight, 
	username) VALUES (%s, %s, %s, %s, %s)"""
	query_info = (parcel_info['nickname'], parcel_info['pickup'], parcel_info['destination'],
	 parcel_info['weight'], current_user)

	db.insert(query_sql, query_info)

	return jsonify({"added parcel": parcel_info['nickname']}), 201

@app.route(base_url + '/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def gets_single_parcel_by_id(parcel_id):

	current_user= get_jwt_identity()

	get_by_user= "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}' " \
	.format(current_user, parcel_id)
	if not db.query(get_by_user):
		return jsonify({"error":"unauthorized access"}), 401

	return jsonify({"item info": db.query(get_by_user)}), 200


@app.route(base_url + '/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
def cancel_order(parcel_id):

	current_user= get_jwt_identity()

	get_by_user= "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}' " \
	.format(current_user, parcel_id)
	if not db.query(get_by_user):
		return jsonify({"error":"unauthorized access"}), 401

	get_by_user = "SELECT * from parcel WHERE username = '{}' and admin = False".format(current_user)

	update_status= "UPDATE parcel set status = %s where parcel_id = %s "

	db.insert(update_status, ("cancelled", parcel_id))

	return jsonify({"cancelled item id: ": parcel_id}), 201


@app.route(base_url + '/auth/user', methods=['POST'])
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
		return jsonify({"error": "usename Already Exists!"}), 400

	db.insert(query_sql, query_info)

	return jsonify({"Register message": "Succesfully registerd to sendIT"}), 201


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
def parcel_status(parcel_id):
	data = request.get_json()

	current_admin= get_jwt_identity()

	get_by_user= "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}'".format(current_admin, parcel_id)
	if not db.query(get_by_user):
		return jsonify({"error":"unauthorized access"}), 401

	get_by_admin = "SELECT * from parcel WHERE username = '{}' and admin = True".format(current_admin)

	update_status= "UPDATE parcel set status = %s where parcel_id = %s "

	db.insert(update_status, (data['status'], parcel_id))

	return jsonify({"status of parcel": data['status']}), 201

@app.route(base_url + '/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
def change_destination_by_user(parcel_id):

	data = request.get_json()

	current_user= get_jwt_identity()

	get_by_user= "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}'".format(current_user, parcel_id)
	if not db.query(get_by_user):
		return jsonify({"error":"unauthorized access"}), 401

	update_dest= "UPDATE parcel set destination = %s where parcel_id = %s "
	db.insert(update_dest, (data['destination'], parcel_id))

	return jsonify({"updated destination to": data['destination']}), 201
