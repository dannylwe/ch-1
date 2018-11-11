import datetime

parcels = []

class Parcel:

	parcel_status = 'pending'

	def __init__(self, nickname, height, width, destination, pickup):
		self.nickname = nickname
		self.height = height
		self.width = width
		self.destination = destination
		self.pickup = pickup
		

	def __repr__(self):
		return 'Initialized parcel object {} with {} pickup location and destination {}'.format(self.nickname,
			self.pickup, self.destination)


def create(payload):
	post = payload
	post['id'] = parcels[-1]['id'] + 1 if len(parcels) > 0 else 100
	post['status'] = Parcel.parcel_status
	post['user_id'] = 1
	post['time'] = datetime.datetime,now()

	parcel_result = Parcel(post['nickname'], post['height'], post['destination'], post['pickup'])
	parcels.append(parcel_result)
	return parcels

parcel_result = Parcel('mums flowers', 11, 14, 'kampala', 'mbarara')
print(parcel_result)
parcel_result = parcel_result.__dict__
#parcel_result['time'] = datetime.datetime.now()
print(parcel_result)

# class Parcel_Store:

# 	parcels = []


# 	@classmethod
# 	def 