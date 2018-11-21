from flask import jsonify, abort
import re

class Verify:

	def error_handler(payload):

		post_parcel = payload

		if not isinstance(post_parcel['height'], int) or not isinstance(post_parcel['weight'], int):
			abort(400, "height and weight must be integers")
		if not isinstance(post_parcel['nickname'], str) or not isinstance(post_parcel['destination'], str) \
		or not isinstance(post_parcel['pickup'], str):
			abort(400, "nickname, destination must be strings")
		if (post_parcel['nickname'].isspace() | post_parcel['weight'].isspace() 
		| post_parcel['height'].isspace() | post_parcel['destination'].isspace() 
		| post_parcel['pickup'].isspace() ):

			abort(400, "fields can not be a space")

		if post_parcel['weight'] > 11:
			return jsonify({"error": "parcel weight is beyond limits"})

		if len(post_parcel['nickname']) < 4:
			return jsonify({"error": "nickname must be at least 4 characters"})

		lower_case = re.complie('[a-z]+')
		if not lower_case.match(post_parcel['nickname']) or not lower_case.match(post_parcel['destination']) \
		or not lower_case.match(post_parcel['pickup']):
			return jsonify({"error": "nickname can only be in lowercase"})
		if (len(post_parcel['height']) or post_parcel['weight']) > 3:
			return jsonify({"error": "invalid lenght of weight or height"})
		return