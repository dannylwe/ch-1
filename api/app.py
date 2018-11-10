from flask import Flask, abort, request, jsonify
from flask_restplus import Api, Resource, fields, abort
from werkzeug.contrib.fixers import ProxyFix
#import uuid

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='sendIT api',
    description='sendIT MVC api',
)

base_url= '/api/v1'

app.config['RESTPLUS_VALIDATE'] = True
app.config['DEBUG'] = True

a_parcel = api.model('parcel', {	
	"nickname": fields.String('Nickname of parcel'), 
	"height": fields.Integer('Height of parcel'),
	"width": fields.Integer('Width of parcel'),
	"destination": fields.String('Destination of parcel'),
	"pickup": fields.String('Pickup location of parcel'),

})

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
		#self.parcels= []

	def gets(self):
		return parcels

	@classmethod
	def create(self, payload):
		post = payload
		post['id'] = parcels[-1]['id'] + 1 if len(parcels) > 0 else 0
		post['status'] = Parcel.parcel_status
		#post['uuid'] = Parcel.uq
		parcels.append(post)
		return parcels

	@classmethod
	def updates(self, id, payload):
		# post = payload
		# if post['id'] != parcels['id']:
		# 	return {"item": "not found"}
		# post.update(payload)
		# return parcels
		# data = payload
		# for new_post in parcels:
		# 	if data['id'] not in new_post['id']:
		# 		raise ValueError('Invalid search') 
		# 	new_post.update(data)
		# 	return parcels
		result = [prod for prod in parcels if prod['id'] == id]
		final = result.update()


	@classmethod
	def get_by_id(self, id):
		result = [prod for prod in parcels if prod['id'] == id]
		return result

@api.route(base_url + '/hello')
class HelloWorld(Resource):

	def get(self):

		"sanity check"

		return {'hello': 'world'}

@api.route(base_url + '/parcel')
class Parcel_info(Resource):

	def get(self):

		"get all parcel info"

		if parcels == []:
			return {"message": "list is empty"}, 200

		return parcels, 200

	@api.expect(a_parcel, validate=True)
	def post(self):

		"post parcel information"
		
		post = api.payload
		Parcel.create(post)

		return {"created": post}, 201

	@api.expect(a_parcel, validate=True)
	def put(self):

		"Place entire parcel"

		post = api.payload
		Parcel.create(post)

		return {"accepted": post}, 202

@api.route(base_url + '/parcel/<int:id>')
class Parcel_by_id(Resource):
	def get(self, id):

		"get by id"

		result = [prod for prod in parcels if prod['id'] == id]

		if result == []:
			return {"message": "nothing here"}, 204

		return result, 200


@app.route(base_url + '/parcel/<int:parcel_id>', methods=['PUT'])
def update_parcel(parcel_id):


	if not parcel_id or parcel_id < 1:
		abort(400, 'Bad request')

	data = request.get_json()

	nickname = data['nickname'],
	height = data['height'],
	width= data['width'], 
	destination = data['destination'],
	pickup = data['pickup']

	new_update = dict(nickname= nickname,
		height= height,
		width =width,
		destination= destination,
		pickup=pickup)

	for parcel in parcels:
		if parcel['parcel_id'] == parcels['id']:
			parcels.append(new_update)

			return jsonify({"message": "updated"}), 202

		return jsonify({"message": "parcel not found"}), 200




