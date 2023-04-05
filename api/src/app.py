import os
import cloudinary
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS 
from flask_jwt_extended import JWTManager
from models import db
from config import DevelopmentConfig, CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
from routes import main
from routes.admin import roles
from routes.admin import users
from routes import messages, auth, profiles

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade, db downgrade
jwt = JWTManager(app)
CORS(app)

cloudinary.config(
  cloud_name = CLOUDINARY_CLOUD_NAME,
  api_key = CLOUDINARY_API_KEY,
  api_secret = CLOUDINARY_API_SECRET,
  secure = True
)

app.register_blueprint(main.bpMain)
app.register_blueprint(roles.bpRole, url_prefix='/api/admin')
app.register_blueprint(users.bpUser, url_prefix='/api/admin')
app.register_blueprint(messages.bpMessage, url_prefix='/api')
app.register_blueprint(auth.bpAuth, url_prefix='/api')
app.register_blueprint(profiles.bgUP, url_prefix='/api')

if __name__ == '__main__':
    app.run()

