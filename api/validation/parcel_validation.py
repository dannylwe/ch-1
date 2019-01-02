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
    if (post_parcel['nickname'].isspace() | post_parcel['destination'].isspace() |
            post_parcel['pickup'].isspace()):

      abort(400, "fields can not be a space")

    if post_parcel['weight'] > 11:
      abort(400, "parcel weight is beyond limits")

    if len(post_parcel['nickname']) < 4:
      abort(400, "nickname must be at least 4 characters")

    lower_case = re.compile('[a-z]+')
    if not lower_case.match(post_parcel['nickname']):
      abort(400, "nickname can only be in lowercase")

    return
