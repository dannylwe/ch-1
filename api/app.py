from flask import Flask, abort, request, jsonify, abort
from werkzeug.contrib.fixers import ProxyFix
#import uuid

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
base_url= '/api/v1'

app.config['DEBUG'] = True

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
		post['id'] = parcels[-1]['id'] + 1 if len(parcels) > 1 else 1
		post['status'] = Parcel.parcel_status
		post['user_id'] = len(parcels) + 1
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
	return {'hello': 'world'}

@app.route(base_url + '/parcel', methods=['GET', 'POST'])
def get_parcel():
	if request.method == 'GET':
		if parcels == []:
			return jsonify({"message": "list is empty"}), 200

		return jsonify({parcels}), 200

	if request.method == 'POST':
		post_parcel = request.get_json()
		Parcel.create(post_parcel)

		return jsonify({"created": post_parcel}), 201

@app.route(base_url + '/parcel/<int:id>', methods=['GET', 'PUT'])
def gets_by_id():

	if request.method == 'GET':
		if type(id) != int:
			abort(400, 'Bad request')

		result = [prod for prod in parcels if prod['id'] == id]
		if result == []:
			return jsonify({"message": "nothing here"}), 204

		return jsonify({result}), 200

	if request.method == 'PUT':

		if not parcel_id or parcel_id < 1:
			abort(400, 'Bad parcel request')

		update_parcel_by_id = request.get_json()
		for item in parcels:
			if update_parcel_by_id['id'] == item['id']:
				parcels.update(update_parcel_by_id)

	return jsonify({"updated": update_parcel_by_id}), 201

@app.route(base_url + '/users/<int:user_id>/parcels', methods=['GET'])
def get_from_user():
	if not user_id or user_id < 1:
		abort(400, 'Bad user request')

	if type(user_id) != int:
		abort(400, 'Bad request')

		result = [prod for prod in parcels if prod['user_id'] == user_id]
		if result == []:
			return jsonify({"message": "nothing here"}), 204

		return jsonify({result}), 200


# @app.route(base_url + '/parcel/<int:parcel_id>', methods=['PUT'])
# def update_parcel(parcel_id):


# 	if not parcel_id or parcel_id < 1:
# 		abort(400, 'Bad request')

# 	data = request.get_json()

# 	nickname = data['nickname'],
# 	height = data['height'],
# 	width= data['width'], 
# 	destination = data['destination'],
# 	pickup = data['pickup']

# 	new_update = dict(nickname= nickname,
# 		height= height,
# 		width =width,
# 		destination= destination,
# 		pickup=pickup)

# 	for parcel in parcels:
# 		if parcel['parcel_id'] == parcels['id']:
# 			parcels.append(new_update)

# 			return jsonify({"message": "updated"}), 202

# 		return jsonify({"message": "parcel not found"}), 200




