import datetime
from marshmallow import Schema, fields
from flask import abort, jsonify

parcels = []


class Parcel:

  parcel_status = 'pending'

  def __init__(self, nickname, height, weight, destination, pickup):
    self.nickname = nickname
    self.height = height
    self.weight = weight
    self.destination = destination
    self.pickup = pickup
    self.created_at = datetime.datetime.now()
    self.status = Parcel.parcel_status

  def __repr__(self):
    return 'Initialized parcel object {} with {} pickup location and destination {}'.format(self.nickname,
                                                                                            self.pickup, self.destination)


class ParcelSchema(Schema):

  nickname = fields.Str()
  height = fields.Int()
  weight = fields.Int()
  destination = fields.Str()
  pickup = fields.Str()
  created_at = fields.DateTime()
  status = fields.Str()


def create(payload):

  post = payload
  parcel_obj = Parcel(post['nickname'], post['height'], post[
                      'weight'], post['destination'], post['pickup'])
  # pprint(parcel_obj)

  schema = ParcelSchema()
  parcel_DTO = schema.dump(parcel_obj)
  parcel_result = parcel_DTO.data
  print(parcel_DTO.errors)

  post['id'] = parcels[-1]['id'] + 1 if len(parcels) > 0 else 100
  post['status'] = Parcel.parcel_status
  post['user_id'] = 1

  parcel_result.update(post)

  parcels.append(parcel_result)
  return parcels


def error_handler(payload):

  post_parcel = payload

  if not isinstance(post_parcel['height'], int) or not isinstance(post_parcel['weight'], int):
    abort(400, "height and weight must be integers")
  if not isinstance(post_parcel['nickname'], str) or not isinstance(post_parcel['destination'], str) or not isinstance(post_parcel['pickup'], str):
    abort(400, "nickname, destination must be strings")
  return
