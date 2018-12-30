from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
#import uuid
from api.models.parcel_store import *
from api.database.dataBase import Database
from api.controller.parcelController import Parcel

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True

app.wsgi_app = ProxyFix(app.wsgi_app)
base_url= '/api/v1'

@app.route(base_url + '/hello')
def hello_world():
	return Parcel.helloWorld()

@app.route(base_url + '/parcels', methods=['GET', 'POST'])
def get_parcel():

	if request.method == 'GET':
		return Parcel.getAllParcels()

	if request.method == 'POST':
		return Parcel.postSingleParcel()

@app.route(base_url + '/parcels/<int:id>', methods=['GET'])
def gets_by_id(id):

	if request.method == 'GET':
		return Parcel.parcelById(id)

@app.route(base_url + '/users/<int:user_id>/parcels', methods=['GET'])
def get_from_user(user_id):
	return Parcel.parcelGetByUserId(user_id)

@app.route(base_url + '/parcels/<int:id>/cancel', methods=['PUT'])
def cancel_order(id):
	return Parcel.parcelCancelById(id)
