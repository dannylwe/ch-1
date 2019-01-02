from unittest import TestCase
import json
from api.views.app import app, base_url
from api.database.dataBase import Database


class BaseTest(TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.db = Database()

	def test_register_user_fail(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"userk", "email":"user1@gmail.com",
				"password":"abcd", "handphone":772504771}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_register_user_exists(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2", "email":"user2@gmail.com",
				"password":"abcdefghij", "handphone":772504771}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_register_email_short(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2", "email":"u@gmail.com",
				"password":"abcdefghij", "handphone":772504771}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_register_password_short(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2", "email":"user1@gmail.com",
				"password":"abcd", "handphone":772504771}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_not_valid_email(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2", "email":"####.com",
				"password":"abcd", "handphone":772504771}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_handphone_is_not_int(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2", "email":"user1@gmail.com",
				"password":"abcd", "handphone":"772504771"}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_username_too_long(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2wwhjdnhniqnkjnwdkndwukhqwdbywbqwyddqwdkjndqwjfewh", 
				"email":"user2@gmail.com",
				"password":"abcdefghij", "handphone":772504771}),content_type="application/json")
		print(response.data)
		self.assertEqual(response.status_code, 400)

	def test_register_user_long_number(self):
		response= self.app.post(base_url + '/auth/user',
			data=json.dumps({"username":"user2", "email":"user1@gmail.com",
				"password":"abcdefghij", "handphone":7725047715759393}),
			content_type="application/json")
		print(response.data)
		#400
		self.assertEqual(response.status_code, 400)

	def test_register_user_exists(self):
		response= self.app.post(base_url + '/auth/login',
			data=json.dumps({"username":"user2", "email":"user1@gmail.com",
				"password":"abcdefghij", "handphone":772504771}),
			content_type="application/json")
		print(response.data)
		#400
		self.assertEqual(response.status_code, 401)

	def test_auth_login_cert(self):
		return self.app.post(base_url + '/auth/login',
			data=json.dumps({"username":"user2", "password":"abcdefghij"}),
			content_type="application/json")