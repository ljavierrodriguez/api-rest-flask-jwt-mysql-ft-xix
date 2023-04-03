from models import Role
from flask import Blueprint, jsonify, request

bpRole = Blueprint('bpRole', __name__)

@bpRole.route('/roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    roles = list(map(lambda role: role.serialize(), roles))
    return jsonify(roles), 200

@bpRole.route('/roles', methods=['POST'])
def create_role():
    name = request.json.get('name')
    found = Role.query.filter_by(name=name).first()
    if found:
        return jsonify({ "status": "400", "message": "Role already exists" }), 400

    role = Role()
    role.name = name
    role.save()

    return jsonify({ "status": "201", "message": "Role created", "role": role.serialize() }), 201

@bpRole.route('/roles/<int:id>', methods=['PUT'])
def update_role(id):
    name = request.json.get('name')

    role = Role.query.get(id)

    if not role:
        return jsonify({ "status": "404", "message": "Role not found" }), 404

    found = Role.query.filter_by(name=name).first()
    if found and id != found.id:
        return jsonify({ "status": "400", "message": "Role already exists" }), 400

    role.name = name
    role.update()

    return jsonify({ "status": "200", "message": "Role updated", "role": role.serialize() }), 200

@bpRole.route('/roles/<int:id>', methods=['DELETE'])
def delete_role(id):
    role = Role.query.get(id)

    if not role:
        return jsonify({ "status": "404", "message": "Role not found" }), 404

    role.delete()

    return jsonify({ "status": "200", "message": "Role deleted", "role": {} }), 200

