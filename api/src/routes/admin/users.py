from models import User, Profile, Role
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_full_info(), users))

    return jsonify({"status": "200", "message": "List of users", "results": users}), 200

@bpUser.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user_by_id(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"status": "404", "message": "User not found"}), 404

    return jsonify({ "status": "200", "message": "User info", "user": user.serialize_full_info()}), 200

@bpUser.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    email = request.json.get('email')
    password = request.json.get('password')
    is_active = request.json.get('is_active', True)
    roles = request.json.get('roles')

    if not email:
        return jsonify({ "status": "422", "message": "Email is required"}), 422
    if not password:
        return jsonify({ "status": "422", "message": "Password is required"}), 422
    if not roles:
        return jsonify({ "status": "422", "message": "Role is required"}), 422

    

    profile = Profile()

    user = User()
    user.email = email
    user.password = generate_password_hash(password)
    user.is_active = is_active
    user.profile = profile

    if len(roles) > 0:
        for id in roles:
            role = Role.query.get(id)
            if role:
                user.roles.append(role)

    user.save()

    if not user: 
        return jsonify({ "status": "400", "message": "User not created", "user": {}}), 400

    return jsonify({ "status": "201", "message": "User created", "user": user.serialize()}), 201

@bpUser.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    pass

@bpUser.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    pass