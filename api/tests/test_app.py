from unittest import TestCase
import json
from api.views.app import app
from api.tests.test_base import BaseTest
from api.database.dataBase import Database

class Test(BaseTest):

	def test_token_refresh(self):
		response = self.app.get('api/v1/token/refresh')
		self.assertEqual(response.status_code, 401)

	def test_parcels_with_posts_invalid_no_auth(self):
		response = self.app.post('api/v1/parcels',
			data = 
			json.dumps({"height": "5", "pickup":"kampala","nickname": "mum's flowers",
				"weight": 10,"destination": "gulu"}),
			content_type="application/json")
		self.assertEqual(response.status_code, 401)

	def test_logout_fail(self):
		response = self.app.get('/api/v1/auth/logout')
		self.assertEqual(response.status_code, 401)

	def teardown():
		super.db.teardown()
