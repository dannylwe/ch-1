from unittest import TestCase
import json
from api.views.app import app


class Test(TestCase):

  def setUp(self):
    self.app = app.test_client()

  def test_hello_world(self):
    response = self.app.get('/api/v1/hello')
    self.assertEqual(response.status_code, 200)

  def test_parcels_no_post(self):
    response = self.app.get('/api/v1/parcels')
    self.assertEqual(response.status_code, 200)

  def test_parcels_with_posts_invalid(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": "5", "pickup": "kampala", "nickname": "mum's flowers", "weight": 10, "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts_invalid_2(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 2, "pickup": 5, "nickname": "mum's flowers", "weight": 10, "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts_invalid_3(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 2, "pickup": "gulu", "nickname": 5, "weight": 10, "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts_invalid_4(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 2, "pickup": "gulu", "nickname": "mums dentist", "weight": "10", "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts_invalid_5(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 2, "pickup": "gulu", "nickname": "patrick", "weight": 10, "destination": 67}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts_invalid_6(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 2, "pickup": "gulu", "nickname": "patrick", "weight": 11, "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": "10", "pickup": "kampala", "nickname": "dental floss", "weight": "5", "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 400)

  def test_parcels_with_posts_ok(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 9, "pickup": "kampala", "nickname": "dental floss", "weight": 5, "destination": "gulu"}),
                             content_type="application/json")
    self.assertEqual(response.status_code, 201)

  def test_parcels_success_get(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 9, "pickup": "kampala", "nickname": "dental floss", "weight": 5, "destination": "gulu"}),
                             content_type="application/json")

    with response:
      response2 = self.app.get('/api/v1/parcels/100')
      self.assertEqual(response2.status_code, 200)

  def test_parcels_success_get_all(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 9, "pickup": "kampala", "nickname": "dental floss", "weight": 5, "destination": "gulu"}),
                             content_type="application/json")

    with response:
      response2 = self.app.get('/api/v1/parcels')
      self.assertEqual(response2.status_code, 200)

  def test_parcels_int(self):
    response = self.app.get('/api/v1/parcels/100')
    self.assertEqual(response.status_code, 200)

  def test_parcels_by_user(self):
    response = self.app.get('/api/v1/users/1/parcels')
    self.assertEqual(response.status_code, 404)

  def test_parcels_success_get_user(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 9, "pickup": "kampala", "nickname": "dental floss", "weight": 5, "destination": "gulu"}),
                             content_type="application/json")

    with response:
      response2 = self.app.get('/api/v1/users/1/parcels')
      self.assertEqual(response2.status_code, 200)

  def test_parcels_success_cancel(self):
    response = self.app.post('/api/v1/parcels',
                             data=json.dumps(
                                 {"height": 9, "pickup": "kampala", "nickname": "dental floss", "weight": 5, "destination": "gulu"}),
                             content_type="application/json")

    with response:
      response2 = self.app.put('/api/v1/parcels/1/cancel')
      response3 = self.app.put('/api/v1/parcels/100/cancel')
      self.assertEqual(response2.status_code, 200)
      self.assertEqual(response3.status_code, 201)
