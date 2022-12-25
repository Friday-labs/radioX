####
'''
Copyright by Friday
'''
###
from flask import Flask
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo

mongo = PyMongo()
#login_manager = LoginManager()
flask_bcrypt = Bcrypt()


def register_extensions(app):
    mongo.init_app(app)
    flask_bcrypt.init_app(app)
    # login_manager.init_app(app)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app

