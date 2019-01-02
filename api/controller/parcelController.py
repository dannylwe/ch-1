from flask import Flask, abort, request, jsonify, abort, make_response
from api.validation.parcel_validation import Verify
from api.validation.user_auth import Auth_user
from api.views import cred_auth_users
from api.models.parcel_store import *
from api.database.dataBase import Database
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                jwt_refresh_token_required, create_refresh_token,
                                get_jwt_identity, set_access_cookies,
                                set_refresh_cookies, unset_jwt_cookies)

db = Database()


class Parcels:

  def postSingleParcel():
    parcel_info = request.get_json()
    current_user = get_jwt_identity()
    time_now = datetime.datetime.now().isoformat()

    Verify.error_handler(parcel_info)

    query_sql = """INSERT INTO parcel (nickname, pickup, destination, weight, 
		username, order_time) VALUES (%s, %s, %s, %s, %s, %s)"""
    query_info = (parcel_info['nickname'], parcel_info['pickup'], parcel_info['destination'],
                  parcel_info['weight'], current_user, time_now)

    db.insert(query_sql, query_info)

    return jsonify({"added parcel": parcel_info['nickname']}), 201

  def getParcelsByUser():
    current_user = get_jwt_identity()
    query_sql_by_user = "SELECT * FROM parcel WHERE username = '{}' ORDER BY order_time ASC".format(
        current_user)

    if not db.query(query_sql_by_user):
      return jsonify({"error": "unauthorized access"}), 401

    resp = jsonify({"item info": db.query(query_sql_by_user)})
    return resp, 200

  def getParcelById(parcel_id):
    current_user = get_jwt_identity()

    get_by_user = "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}' " \
        .format(current_user, parcel_id)
    if not db.query(get_by_user):
      return jsonify({"error": "unauthorized access"}), 401

    return jsonify({"item info": db.query(get_by_user)}), 200

  def cancelById(parcel_id):
    current_user = get_jwt_identity()

    get_by_user = "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}' " \
        .format(current_user, parcel_id)
    if not db.query(get_by_user):
      return jsonify({"error": "unauthorized access"}), 401

    get_by_user = "SELECT * from parcel WHERE username = '{}' and admin = False".format(
        current_user)

    update_status = "UPDATE parcel set status = %s where parcel_id = %s "

    db.insert(update_status, ("cancelled", parcel_id))

    return jsonify({"cancelled item id: ": parcel_id}), 201

  def refreshToken():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    resp = jsonify(
        {'message': 'Refreshed access token. You can now continue using sendIT'})
    set_access_cookies(resp, access_token)
    return resp, 200

  def adminStatusUpdate(parcel_id):
    data = request.get_json()

    current_user = get_jwt_identity()
    query_sql_by_admin = "SELECT * FROM users WHERE username = '{}' AND admin = True".format(
        current_user)

    if not db.query(query_sql_by_admin):
      return jsonify({"error": "unauthorized access, not admin"}), 401

    update_status = "UPDATE parcel set status = %s where parcel_id = %s "

    db.insert(update_status, (data['status'], parcel_id))

    return jsonify({"status of parcel": data['status']}), 201

  def changeDestination(parcel_id):
    data = request.get_json()

    current_user = get_jwt_identity()

    get_by_user = "SELECT * from parcel WHERE username = '{}' and parcel_id= '{}'".format(
        current_user, parcel_id)
    if not db.query(get_by_user):
      return jsonify({"error": "unauthorized access"}), 401

    update_dest = "UPDATE parcel set destination = %s where parcel_id = %s "
    db.insert(update_dest, (data['destination'], parcel_id))

    return jsonify({"updated destination to": data['destination']}), 201

  def getDelivered():
    current_user = get_jwt_identity()
    query_sql_by_user_dest = "SELECT * FROM parcel WHERE username = '{}' AND status = 'delivered' ".format(
        current_user)

    if not db.query(query_sql_by_user):
      return jsonify({"error": "unauthorized view access"}), 401

    resp = jsonify({"item info": db.query(query_sql_by_user_dest)})
    return resp, 200

  def adminAllParcels():
    current_user = get_jwt_identity()
    query_sql_by_admin = "SELECT * FROM users WHERE username = '{}' AND admin = True".format(
        current_user)

    if not db.query(query_sql_by_admin):
      return jsonify({"error": "unauthorized access, not admin"}), 401

    get_all_parcels = "SELECT * FROM parcel WHERE status != 'cancelled';"

    resp = jsonify({"item info": db.query(get_all_parcels)})
    return resp, 200
