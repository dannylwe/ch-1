from flask import Flask, abort, request, jsonify, abort, make_response
from flask_cors import CORS, cross_origin
import datetime
from api.models.parcel_store import *
from api.database.dataBase import Database
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                jwt_refresh_token_required, create_refresh_token,
                                get_jwt_identity, set_access_cookies,
                                set_refresh_cookies, unset_jwt_cookies)
from api.validation.parcel_validation import Verify
from api.validation.user_auth import Auth_user
from api.views import cred_auth_users
from api.controller.parcelController import Parcels

app = Flask(__name__)
db = Database()
db.create_table()
app.register_blueprint(cred_auth_users.blueprint)

CORS(app, supports_credentials=True)
jwt = JWTManager(app)

app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'THANOS-wilL-RetUrn'
app.config['JWT_TOKEN_LOCATION'] = "cookies"
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

token_expire = datetime.timedelta(days=0.1)

base_url = '/api/v1'


@app.route(base_url + '/parcels', methods=['POST', 'GET'])
@jwt_required
def post_single_parcel():
  """post single parcel"""
  if request.method == 'POST':
    return Parcels.postSingleParcel()

  else:
    """get parcels belonging to single user by Id"""
    return Parcels.getParcelsByUser()


@app.route(base_url + '/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def gets_single_parcel_by_id(parcel_id):
  """get single parcel by Id"""
  return Parcels.getParcelById(parcel_id)


@app.route(base_url + '/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
def cancel_order(parcel_id):
  """cancel a single parcel by Id"""
  return Parcels.cancelById(parcel_id)


@app.route(base_url + '/token/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh_token():
  """refresh token upon expiry"""
  return Parcels.refreshToken()


@app.route(base_url + '/parcels/<int:parcel_id>/status', methods=['PUT'])
@jwt_required
def parcel_status(parcel_id):
  """admin update the status of parcel"""
  return Parcels.adminStatusUpdate(parcel_id)


@app.route(base_url + '/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
def change_destination_by_user(parcel_id):
  """user changes destination of parcel"""
  return Parcels.changeDestination(parcel_id)


@app.route(base_url + '/parcels/delivered', methods=['GET'])
@jwt_required
def get_all_destination():
  """get delivered items for user"""
  return Parcels.getDelivered()


@app.route(base_url + '/parcels/all', methods=['GET'])
@jwt_required
def get_all_parcels_admin():
  """admin has view of all parcels"""
  return Parcels.adminAllParcels()
