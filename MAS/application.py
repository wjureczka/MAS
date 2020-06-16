from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://MAS:MAS@localhost:5432/MAS"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['JWT_SECRET_KEY'] = 'MAS_SECRET_KEY'  # Change this!

jwt = JWTManager(application)
db = SQLAlchemy(application)
migrate = Migrate(application, db)

from MAS.models.Users.User import User
from MAS.models.Users.Tenant import Tenant
from MAS.models.Users.LandLord import LandLord
from MAS.models.Group import Group
from MAS.models.User_Group import User_Group

from MAS.controllers.UserController import *
from MAS.controllers.GroupController import *
from MAS.controllers.AuthController import *
