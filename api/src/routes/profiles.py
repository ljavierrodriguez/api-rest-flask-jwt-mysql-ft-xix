from flask import Blueprint, request, jsonify
from cloudinary.uploader import upload
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User

bgUP = Blueprint('bpUP', __name__)

@bgUP.route('/avatar', methods=['POST'])
@jwt_required()
def upload_avatar():

    if not 'avatar' in request.files:
        return jsonify({ "status": 422, "message": "Avatar is required"}), 422

    id = get_jwt_identity() # Obtener el id del usuario que esta log in
    avatar = request.files['avatar'] # Obtener la imagen o el archivo que estamos recibiendo 
    user = User.query.get(id) # buscamos el usuario a modificar
    public_id = "avatar_user_" + str(id) # generamos un id para la imagen

    print(public_id)

    resp = upload(avatar, public_id=public_id, folder="avatars") # hacemos el upload de la imagen al servidor (cloudinary)
    
    if resp:

        user.profile.avatar = resp['secure_url']
        user.profile.avatar_public_id = resp['public_id']
        user.update()

        return jsonify({"status": 200, "message": "Avatar Uploaded", "result": user.serialize_full_info()}), 200

    else:
        
        return jsonify({ "status": 400, "message": "Please try again later"}), 400

