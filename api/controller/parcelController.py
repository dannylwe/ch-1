from flask import Flask, abort, request, jsonify, abort, make_response
from api.models.parcel_store import *


class Parcel:

  def __init__(self):
    pass

  def helloWorld():
    return jsonify({'hello': 'world'}), 200

  def getAllParcels():
    if parcels == []:
      return jsonify({"message": "list is empty"}), 200
    return jsonify({"message": parcels}), 200

  def postSingleParcel():
    post_parcel = request.get_json()

    error_handler(post_parcel)

    if post_parcel['weight'] > 10:
      abt_weight = make_response("Too heavy")
      abt_weight.status_code = 400
      return abt_weight

    create(post_parcel)

    return jsonify({"created": post_parcel}), 201

  def parcelById(id):
    result = [prod for prod in parcels if prod['id'] == id]

    if result == []:
      return jsonify({"message": "nothing here"}), 200
    return jsonify({"message": result}), 200

  def parcelGetByUserId(user_id):
    result = []

    for users in parcels:
      if users['user_id'] == user_id:
        result.append(users)

    if result == []:
      abort(404, 'No such user')
    return jsonify({"message": result})

  def parcelCancelById(id):
    for parcel in parcels:
      if parcel['id'] == id:
        parcel['status'] = "cancelled"
        return jsonify({"cancelled": parcel}), 201
      return jsonify({"message": "Id does not exist"}), 200
