from models import User, Message
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bpMessage = Blueprint('bpMessage', __name__)

@bpMessage.route('/messages', methods=['GET'])
@jwt_required()
def get_all_messages():
    messages = Message.query.all()
    messages = list(map(lambda msg: msg.serialize(), messages))

    return jsonify({ "status": 200, "messages": "List of messages", "results": messages}), 200


@bpMessage.route('/messages', methods=['POST'])
@jwt_required()
def send_message():

    message = request.json.get('message')
    from_id = request.json.get('from_id')
    to_id = request.json.get('to_id')

    msg = Message()
    msg.message = message
    msg.from_id = from_id
    msg.to_id = to_id

    msg.save()

    return jsonify({ "status": 201, "messages": "Message sent", "result": msg.serialize()}), 200


@bpMessage.route('/messages/<int:id>', methods=['POST'])
@jwt_required()
def delete_message(id):
    msg = Message.query.get(id)

    if not msg:
        return jsonify({ "status": 404, "message": "Message not found"}), 404
    msg.delete()
    
    return jsonify({ "status": 200, "message": "Message deleted", "result": {}}), 200

