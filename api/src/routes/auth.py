import datetime
from models import User, Profile, Role
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

bpAuth = Blueprint('bpAuth', __name__)

@bpAuth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        return jsonify({ "status": 422, "message": "Email is required"}), 422
    if not password:
        return jsonify({ "status": 422, "message": "Password is required"}), 422

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({ "status": 401, "message": "Email/Password are incorrects"}), 401

    if not check_password_hash(user.password, password):
        return jsonify({ "status": 401, "message": "Email/Password are incorrects"}), 401

    # token con vencimiento
    expire = datetime.timedelta(minutes=5)
    access_token = create_access_token(identity=user.id, expires_delta=expire)

    # token sin vencimiento
    # access_token = create_access_token(identity=user.id)

    data = {
        "access_token": access_token,
        "user": user.serialize(),
        "expire": expire.total_seconds()
    }

    return jsonify({ "status": 200, "message": "Login successfully.", "data": data}), 200


@bpAuth.route('/register', methods=['POST'])
def register():
    pass

@bpAuth.route('/me')
@jwt_required()
def info_about_me():
    id = get_jwt_identity()
    user = User.query.get(id)

    return jsonify({ "status": 200, "message": "User info", "data": user.serialize_full_info()}), 200