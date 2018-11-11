from unittest import TestCase
import json
import app

class Test(TestCase):

	def setUp(self):
		self.app = app.app.test_client()  

	def test_hello_world(self):
		response = self.app.get('/api/v1/hello')
		self.assertEqual(response.status_code, 200)
	def test_parcels_no_post(self):
		response = self.app.get('/api/v1/parcels')
		self.assertEqual(response.status_code, 200)
	# def test_parcels_with_posts(self):
	# 	response = self.app.post('/api/v1/parcels', data= json.dumps({"height": "tall","pickup": 11,"nickname": "updated","width": 10,"destination": "string"}))
	# 	self.assertEqual(response.status_code, 200)
	def test_parcels_int(self):
		response = self.app.get('/api/v1/parcels/1')
		self.assertEqual(response.status_code, 204)
	def test_parcels_by_user(self):
		response = self.app.get('/users/1/parcels')
		self.assertEqual(response.status_code, 404)