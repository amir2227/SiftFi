from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.MYSQL_CONNECTION_STRING
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["UPLOAD_FOLDER"] = config.UPLOAD_FOLDER
db = SQLAlchemy(app)

from app import auth, user_management, forex, forex_diff