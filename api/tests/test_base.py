from unittest import TestCase
import json
from api.views.app import app

class BaseTest(TestCase):
	
	def setUp(self):
		self.app = app.test_client()

	def test_login(self):
		response= self.app.post('api/v1/auth/user',
			data=json.dumps({"username":"user1", "email":"user1@gmail.com",
				"password":"abcd$", "handphone":772504771}),content_type="application/json")
		self.assertEqual(response.status_code, 400)