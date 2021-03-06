from flask import Flask, abort, request, jsonify, abort, make_response
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
import datetime
#import uuid
from api.models.parcel_store import *
from api.database.dataBase import Database

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True

app.wsgi_app = ProxyFix(app.wsgi_app)
base_url= '/api/v1'

@app.route(base_url + '/hello')
def hello_world():
	return jsonify({'hello': 'world'}), 200

@app.route(base_url + '/parcels', methods=['GET', 'POST'])
def get_parcel():

	if request.method == 'GET':
		if parcels == []:
			return jsonify({"message": "list is empty"}), 200
		return jsonify({"message":parcels}), 200

	if request.method == 'POST':
		post_parcel = request.get_json()

		error_handler(post_parcel)

		if post_parcel['weight'] > 10:
			abt_weight = make_response("Too heavy")
			abt_weight.status_code = 400
			return abt_weight

		create(post_parcel)

		return jsonify({"created": post_parcel}), 201

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


@app.route(base_url + '/register', methods=['POST'])
def register_user():

	user_info = request.get_json()
	db = Database()

	query_sql = """INSERT INTO USERS (email, password, handphone, username) VALUES (%s,
	%s, %s, %s)"""

	query_info = (user_info['email'], user_info['password'], user_info['handphone'],
	 user_info['username'])

	db.insert(query_sql, query_info)

	return jsonify({"Register message": "Succesfully registerd to sendIT"}), 200