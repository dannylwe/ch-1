

from flask import Flask, abort, request, jsonify, abort
#from werkzeug.contrib.fixers import ProxyFix
#import uuid
app = Flask(__name__)

app.config['DEBUG'] = True

#app.wsgi_app = ProxyFix(app.wsgi_app)
base_url= '/api/v1'

parcels = []

class Parcel:

	parcel_status = 'pending'
	#uq = uuid.uuid4()

	def __init__(self, nickname, height, width, destination, pickup):
		self.nickname = nickname
		self.height = height
		self.width = width
		self.destination = destination
		self.pickup = pickup

	def gets(self):
		return parcels

	@classmethod
	def create(self, payload):
		post = payload
		post['id'] = parcels[-1]['id'] + 1 if len(parcels) > 0 else 100
		post['status'] = Parcel.parcel_status
		post['user_id'] = 1
		#post['uuid'] = Parcel.uq
		parcels.append(post)
		return parcels

	# @classmethod
	# def updates(self, id, payload):
	
	# 	result = [prod for prod in parcels if prod['id'] == id]
	# 	final = result.update()


	# @classmethod
	# def get_by_id(self, id):
	# 	result = [prod for prod in parcels if prod['id'] == id]
	# 	return result

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
		Parcel.create(post_parcel)

		return jsonify({"created": post_parcel}), 201

@app.route(base_url + '/parcels/<int:id>', methods=['GET'])
def gets_by_id(id):

	if request.method == 'GET':
		if type(id) != int:
			abort(400, 'No string literal allowed')

		result = [prod for prod in parcels if prod['id'] == id]
		if result == []:
			return jsonify({"message": "nothing here"}), 204

		return jsonify({"message": result}), 200


@app.route(base_url + '/users/<int:user_id>/parcels', methods=['GET'])
def get_from_user(user_id):
	if user_id < 1:
		abort(400, 'Bad user request')

	if type(user_id) != int:
		abort(400, 'Bad request')

	# result = [prod for prod in parcels if prod['user_id'] == user_id]
	# if result == []:
	# 	return jsonify({"message": "nothing here"}), 204

	# return jsonify({"message": result}), 200
	result = []
	for users in parcels:
		if users['user_id'] == user_id:
			result.append(users)
		else: 
			if result == []:
				abort(400, 'No such user')

	return jsonify({"message": result})






