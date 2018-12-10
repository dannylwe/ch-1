from flask import Flask, abort, request, jsonify, abort, make_response
from flask_cors import CORS, cross_origin
import datetime
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

CORS(app, supports_credentials=True)
jwt = JWTManager(app)

app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'THANOS-will-RetUrn'
app.config['JWT_TOKEN_LOCATION'] = "cookies"
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

token_expire = datetime.timedelta(days=0.1)

base_url= '/api/v1'

@app.route(base_url + '/parcels', methods=['POST', 'GET'])
@jwt_required
def post_single_parcel():
	if request.method == 'POST':
		parcel_info = request.get_json()
		current_user = get_jwt_identity()

		Verify.error_handler(parcel_info)

		query_sql = """INSERT INTO parcel (nickname, pickup, destination, weight, 
		username) VALUES (%s, %s, %s, %s, %s)"""
		query_info = (parcel_info['nickname'], parcel_info['pickup'], parcel_info['destination'],
		parcel_info['weight'], current_user)

		db.insert(query_sql, query_info)

		return jsonify({"added parcel": parcel_info['nickname']}), 201

	else:
		current_user = get_jwt_identity()
		query_sql_by_user = "SELECT * FROM parcel WHERE username = '{}'".format(current_user)

		if not db.query(query_sql_by_user):
			return jsonify({"error":"unauthorized access"}), 401

		resp = jsonify({"item info": db.query(query_sql_by_user)})
		return resp, 200

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

@app.route(base_url + '/parcels/destination', methods=['GET'])
@jwt_required
def get_all_destination():
	current_user = get_jwt_identity()
	query_sql_by_user_dest = "SELECT * FROM parcel WHERE username = '{}' AND WHERE status = 'delivered' ".format(current_user)

	if not db.query(query_sql_by_user):
		return jsonify({"error":"unauthorized access"}), 401

	resp = jsonify({"item info": db.query(query_sql_by_user_dest)})
	return resp, 200
