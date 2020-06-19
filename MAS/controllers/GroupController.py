from flask import jsonify, request
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required, decode_token

from MAS.application import application, db
from MAS.models.Group import Group
from MAS.models.User_Group import User_Group
from MAS.models.Users.Tenant import Tenant


@application.route('/groups', methods=['GET'])
@jwt_required
@cross_origin(supports_credentials=True, headers=['Content-Type', 'Authorization'])
def get_groups():
    current_user = get_jwt_identity()

    current_user_id = current_user['id']

    groups = Group.query.join(User_Group).filter_by(tenant_id=current_user_id).all()

    return jsonify(groups)


@application.route('/groups/<int:group_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_group(group_id):
    user = Group.query.get(group_id)

    return jsonify(user)


@application.route('/groups', methods=['OPTIONS', 'POST'])
@cross_origin(supports_credentials=True, headers=['Content-Type', 'Authorization'])
def post_group():
    new_group_data = request.json

    current_user = decode_token(request.cookies.get('access_token_cookie'))

    current_user_id = current_user['identity']['id']

    try:
        new_group = Group(
            preferred_size=new_group_data['preferred_size'],
            preferred_locations=new_group_data['preferred_locations'],
            preferred_room_quantity=new_group_data['preferred_room_quantity'],
            budget=new_group_data['preferred_budget'],
            name=new_group_data['group_name']
        )

        tenant = Tenant.query.filter_by(id=current_user_id).first()

        new_group.users.append(
            tenant
        )

        db.session.add(new_group)
        db.session.commit()
    except AssertionError as assertion_error:
        return jsonify((assertion_error.__str__())), 400

    return jsonify({ 'group_id': new_group.id }), 201


@application.route('/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id: int):
    group_to_delete = Group.query.get(group_id)

    db.session.delete(group_to_delete)
    db.session.commit()

    return ('', 204)

@application.route('/groups/<int:group_id>/add-user', methods=['POST'])
@cross_origin(supports_credentials=True, headers=['Content-Type', 'Authorization'])
def add_user_to_group(group_id: int):
    new_user_email = request.json['email']



    tenant = Tenant.query.filter_by(email=new_user_email).first()

    if tenant is None:
        return '', 404

    group = Group.query.filter_by(id=group_id).first()

    if group is None:
        return '', 404

    try:
        group.users.append(
            tenant
        )
        db.session.commit()
    except AssertionError as assertion_error:
        return jsonify((assertion_error.__str__())), 400

    return '', 200