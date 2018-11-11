import datetime
from marshmallow import Schema, fields, pprint

parcels = []

class Parcel:

	parcel_status = 'pending'

	def __init__(self, nickname, height, width, destination, pickup):
		self.nickname = nickname
		self.height = height
		self.width = width
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
	width = fields.Int()
	destination = fields.Str()
	pickup = fields.Str()
	created_at = fields.DateTime()
	status = fields.Str()

def create(payload):

	post = payload
	parcel_obj = Parcel(post['nickname'], post['height'], post['width'], post['destination'], post['pickup'])
	#pprint(parcel_obj)

	schema = ParcelSchema()
	parcel_DTO = schema.dump(parcel_obj)
	parcel_result= parcel_DTO.data
	print(parcel_DTO.errors)

	post['id'] = parcels[-1]['id'] + 1 if len(parcels) > 0 else 100
	post['status'] = Parcel.parcel_status
	post['user_id'] = 1
	
	parcel_result.update(post)

	parcels.append(parcel_result)
	return parcels

# parcel_result = Parcel('mums flowers', 11, 14, 'kampala', 'mbarara')
# # print(parcel_result)
# # parcel_result = parcel_result.__dict__
# # #parcel_result['time'] = datetime.datetime.now()
# # print(parcel_result)

# schema = ParcelSchema()
# result = schema.dump(parcel_result)
# result = result.data
# # print(result)
# # result['time'] = datetime.datetime.now()
# pprint(result)

# class Parcel_Store:

# 	parcels = []


# 	@classmethod
# 	def 