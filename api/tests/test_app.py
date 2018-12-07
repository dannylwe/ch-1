from unittest import TestCase
import json
from api.views.app import app
from api.tests.test_base import BaseTest
from api.database.dataBase import Database



# dao = BaseTest()

class Test(BaseTest): #inherit basetst

	# def setUp(self):
	# 	self.app = app.test_client()
	# 	self.db = Database() 

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




	# with dao.test_register_user_exists():
	# 	print('hello')



	# def test_hello_world(self):
	# 	response = self.app.get('/api/v1/hello')
	# 	self.assertEqual(response.status_code, 200)

	# def test_parcels_no_post(self):
	# 	response = self.app.get('/api/v1/parcels')
	# 	self.assertEqual(response.status_code, 200)

	# def test_parcels_with_posts_invalid(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": "5", "pickup":"kampala","nickname": "mum's flowers","weight": 10,"destination": "gulu"}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 401)

	# def test_parcels_with_posts_invalid_2(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": 2, "pickup": 5,"nickname": "mum's flowers","weight": 10,"destination": "gulu"}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 400)

	# def test_parcels_with_posts_invalid_3(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": 2, "pickup": "gulu","nickname": 5,"weight": 10,"destination": "gulu"}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 400)

	# def test_parcels_with_posts_invalid_4(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": 2, "pickup": "gulu","nickname": "mums dentist","weight": "10","destination": "gulu"}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 400)

	# def test_parcels_with_posts_invalid_5(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": 2, "pickup": "gulu","nickname": "patrick","weight": 10,"destination": 67}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 400)

	# def test_parcels_with_posts_invalid_6(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": 2, "pickup": "gulu","nickname": "patrick","weight": 11,"destination": "gulu"}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 400)

	# def test_parcels_with_posts(self):
	# 	response = self.app.post('/api/v1/parcels', 
	# 		data = 
	# 		json.dumps({"height": "10", "pickup":"kampala","nickname": "dental floss","weight": "5","destination": "gulu"}),
	# 		content_type="application/json")
	# 	self.assertEqual(response.status_code, 400)

	# def test_parcels_int(self):
	# 	response = self.app.get('/api/v1/parcels/1')
	# 	self.assertEqual(response.status_code, 200)

	# def test_parcels_by_user(self):
	# 	response = self.app.get('/users/1/parcels')
	# 	self.assertEqual(response.status_code, 404)