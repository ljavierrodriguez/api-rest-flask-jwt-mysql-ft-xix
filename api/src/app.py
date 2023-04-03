from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS 
from flask_jwt_extended import JWTManager
from models import db
from config import DevelopmentConfig
from routes import main
from routes.admin import roles

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade, db downgrade
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(main.bpMain)
app.register_blueprint(roles.bpRole, url_prefix='/api/admin')

if __name__ == '__main__':
    app.run()

