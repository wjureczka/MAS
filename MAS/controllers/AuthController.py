from flask import jsonify
from flask_jwt_extended import create_access_token

from MAS.application import application, request, db
from MAS.models.Users.User import User


@application.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    login_user = User.query.filter_by(email=email).first()

    if login_user is None:
        return "Bad request", 400

    if login_user.password is not password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200
