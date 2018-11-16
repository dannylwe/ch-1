from unittest import TestCase
import json
from views.app import app


class Test(TestCase):

	def setUp(self):
		self.app = app.test_client()  

	def test_hello_world(self):
		response = self.app.get('/api/v1/hello')
		self.assertEqual(response.status_code, 200)

	def test_parcels_no_post(self):
		response = self.app.get('/api/v1/parcels')
		self.assertEqual(response.status_code, 200)

	def test_parcels_with_posts(self):
		response = self.app.post('/api/v1/parcels', 
			data = 
			json.dumps({"height": 5, "pickup":"kampala","nickname": "mum's flowers","weight": 10,"destination": "gulu"}),
			content_type="application/json")
		self.assertEqual(response.status_code, 201)

	def test_parcels_int(self):
		response = self.app.get('/api/v1/parcels/1')
		self.assertEqual(response.status_code, 200)

	def test_parcels_by_user(self):
		response = self.app.get('/users/1/parcels')
		self.assertEqual(response.status_code, 404)