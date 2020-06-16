from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from MAS.application import application, db
from MAS.models.Group import Group


@application.route('/groups', methods=['GET'])
@jwt_required
def get_groups():
    current_user = get_jwt_identity()

    users = Group.query.all()

    return jsonify(users)


@application.route('/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    user = Group.query.get(group_id)

    return jsonify(user)


@application.route('/groups', methods=['POST'])
def post_group():
    new_group_data = request.json

    try:
        new_group = Group(
            preferred_size=new_group_data['preferred_size'],
            preferred_locations=new_group_data['preferred_locations'],
            preferred_room_quantity=new_group_data['preferred_room_quantity'],
            budget=new_group_data['budget']
        )

        db.session.add(new_group)
        db.session.commit()
    except AssertionError as assertion_error:
        return (jsonify((assertion_error.__str__())), 400)

    return ('', 201)


@application.route('/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id: int):
    group_to_delete = Group.query.get(group_id)

    db.session.delete(group_to_delete)
    db.session.commit()

    return ('', 204)