from flask import jsonify, request

from MAS.application import application, db
from MAS.models.Group import Group


@application.route('/groups', methods=['GET'])
def GetGroups():
    users = Group.query.all()

    return jsonify(users)


@application.route('/groups/<int:group_id>', methods=['GET'])
def GetGroup(group_id):
    user = Group.query.get(group_id)

    return jsonify(user)


@application.route('/groups', methods=['POST'])
def PostGroup():
    new_group_data = request.json

    try:
        new_group = Group()

        db.session.add(new_group)
        db.session.commit()
    except AssertionError as assertion_error:
        return (jsonify((assertion_error.__str__())), 400)

    return ('', 201)


@application.route('/groups/<int:group_id>', methods=['DELETE'])
def DeleteGroup(group_id: int):
    group_to_delete = Group.query.get(group_id)

    db.session.delete(group_to_delete)

    return ('', 204)