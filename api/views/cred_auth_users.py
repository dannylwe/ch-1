from flask import Blueprint, request, jsonify
from .app import (JWTManager, jwt_required, create_access_token,
jwt_refresh_token_required, create_refresh_token,
get_jwt_identity, set_access_cookies,
set_refresh_cookies, unset_jwt_cookies)
from flask_cors import CORS, cross_origin
from api.database.dataBase import Database
import datetime
from api.validation.user_auth import Auth_user
from api.controller.authController import Auth

db = Database()

base_url= '/api/v1'

blueprint = Blueprint("user_login", __name__)

CORS(blueprint, supports_credentials=True)

@blueprint.route(base_url + '/auth/login', methods=['POST'])
def login_user_auth():
	"""login into sendIT"""
	return Auth.login()

@blueprint.route(base_url + '/auth/user', methods=['POST'])
def register_user():
	"""register user""" 
	return Auth.registerUser()

@blueprint.route(base_url + '/auth/logout', methods=['GET'])
@jwt_required
def logout_revoke_jwt():
	"""logout of application"""
	return Auth.logout()
    
@blueprint.route('/')
def homepage():
	"""index page/landing page"""
	return Auth.landingPage()

@blueprint.route(base_url + '/auth/all/users', methods=['GET'])
def get_all_users():
	"""get all users of application"""
	return Auth.allUsers()