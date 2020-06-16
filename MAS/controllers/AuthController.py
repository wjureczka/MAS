from flask import jsonify, make_response
from flask_jwt_extended import create_access_token

from MAS.application import application, request, db, jwt
from MAS.models.Users.User import User


@application.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return "Missing JSON in request", 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return "Missing username parameter", 400
    if not password:
        return "Missing password parameter", 400

    login_user = User.query.filter_by(email=email).first()

    if login_user is None:
        return "Bad request", 400

    if login_user.password != password:
        return "Bad username or password", 401

    identity = { 'id': login_user.id, 'name': login_user.name, 'email': login_user.email }
    access_token = create_access_token(identity=identity)

    response = make_response(jsonify(access_token=access_token))
    response.set_cookie('access_token', access_token, httponly=True)

    return response
