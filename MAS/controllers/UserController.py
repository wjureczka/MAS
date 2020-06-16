from flask import jsonify, request

from MAS.application import application, db
from MAS.models.Users.User import User


@application.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify(users)


@application.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    return jsonify(user)


@application.route('/users', methods=['POST'])
def post_user():
    new_user_data = request.json

    try:
        new_user = User(
            pesel=new_user_data['pesel'],
            name=new_user_data['name'],
            surname=new_user_data['surname'],
            email=new_user_data['email'],
            password=new_user_data['password']
        )

        db.session.add(new_user)
        db.session.commit()
    except AssertionError as assertion_error:
        return (jsonify((assertion_error.__str__())), 400)

    return ('', 201)
