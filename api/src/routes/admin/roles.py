from models import Role
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

bpRole = Blueprint('bpRole', __name__)

@bpRole.route('/roles', methods=['GET'])
@jwt_required()
def get_roles():
    roles = Role.query.all()
    roles = list(map(lambda role: role.serialize(), roles))
    return jsonify({"status": 200, "message": "List of roles", "results": roles}), 200

@bpRole.route('/roles/<int:id>', methods=['GET'])
@jwt_required()
def get_role_by_id(id):
    role = Role.query.get(id)

    if not role:
        return jsonify({ "status": 404, "message": "Role not found" }), 404

    return jsonify({ "status": 200, "message": "Role Info", "result": role.serialize() }), 201

@bpRole.route('/roles', methods=['POST'])
@jwt_required()
def create_role():
    name = request.json.get('name')
    found = Role.query.filter_by(name=name).first()
    if found:
        return jsonify({ "status": 400, "message": "Role already exists" }), 400

    role = Role()
    role.name = name
    role.save()

    return jsonify({ "status": 201, "message": "Role created", "result": role.serialize() }), 201

@bpRole.route('/roles/<int:id>', methods=['PUT'])
@jwt_required()
def update_role(id):
    name = request.json.get('name')

    role = Role.query.get(id)

    if not role:
        return jsonify({ "status": 404, "message": "Role not found" }), 404

    found = Role.query.filter_by(name=name).first()
    if found and id != found.id:
        return jsonify({ "status": 400, "message": "Role already exists" }), 400

    role.name = name
    role.update()

    return jsonify({ "status": 200, "message": "Role updated", "result": role.serialize() }), 200

@bpRole.route('/roles/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_role(id):
    role = Role.query.get(id)

    if not role:
        return jsonify({ "status": 404, "message": "Role not found" }), 404

    role.delete()

    return jsonify({ "status": 200, "message": "Role deleted", "result": {} }), 200

