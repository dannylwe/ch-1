from flask import Blueprint, request, jsonify
from .app import (JWTManager, jwt_required, create_access_token,
jwt_refresh_token_required, create_refresh_token,
get_jwt_identity, set_access_cookies,
set_refresh_cookies, unset_jwt_cookies, CORS)
from api.database.dataBase import Database
import datetime

token_expire = datetime.timedelta(days=0.1)

db = Database()

base_url= '/api/v1'

blueprint = Blueprint("user_login", __name__)

CORS(blueprint)

@blueprint.route(base_url + '/auth/login', methods=['POST'])

def login_user_auth():

	user_login = request.get_json()

	query_login = "SELECT username, password from users WHERE username = '{}' and password = '{}' ".format(
		user_login['username'], user_login['password'])

	if not db.query(query_login):
		return jsonify({"error": "invalid credentials"}), 401

	access_token= create_access_token(identity= user_login['username'], expires_delta=token_expire)
	refresh_token= create_access_token(identity=user_login['username'], expires_delta=token_expire)
	resp = jsonify({"message": "Logged in successfully. Welcome to sendIT"})

	resp.headers.add('Access-Control-Allow-Origin', '*')

	set_access_cookies(resp, access_token)
	set_refresh_cookies(resp, refresh_token)

	return resp, 200


@blueprint.route(base_url + '/auth/logout', methods=['GET'])
@jwt_required
def logout_revoke_jwt():
    resp = jsonify({'logout': "Logged out of sendIT"})
    unset_jwt_cookies(resp)
    return resp, 200