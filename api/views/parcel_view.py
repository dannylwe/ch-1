from flask import Blueprint, request, jsonify
from .app import (JWTManager, jwt_required, create_access_token,
jwt_refresh_token_required, create_refresh_token,
get_jwt_identity, set_access_cookies,
set_refresh_cookies, unset_jwt_cookies)
from api.database.dataBase import Database
import datetime

Parcel = Blueprint("parcel_view", __name__)

base_url= '/api/v1'

@Parcel.route(base_url + '/parcels', methods=['POST'])
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

@Parcel.route(base_url + '/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
def cancel_order(parcel_id):

	post_parcel = request.get_json()

	error_handler(post_parcel)

	current_user= get_jwt_identity()

	get_by_user= "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}'".format(current_user, parcel_id)
	if not db.query(get_by_user):
		return jsonify({"error":"unauthorized access"}), 401

	get_by_user = "SELECT * from parcel WHERE username = '{}' and admin = False".format(current_user)

	update_status= "UPDATE parcel set status = %s where parcel_id = %s "

	db.insert(update_status, ("cancelled", parcel_id))

	return jsonify({"cancelled": parcel_id}), 201

@Parcel.route(base_url + '/parcels/<int:parcel_id>/status', methods=['PUT'])
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

@Parcel.route(base_url + '/parcels/<int:parcel_id>/destination', methods=['PUT'])
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