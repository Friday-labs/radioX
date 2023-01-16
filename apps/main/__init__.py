'''
***
'''
from typing import Type
from flask import Flask
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_redis import FlaskRedis
from flask_pymongo import PyMongo
from apps.main.config import Config

mongo = PyMongo()
#login_manager = LoginManager()
redis_store = FlaskRedis()
flask_bcrypt = Bcrypt()


def register_extensions(app : Flask):
    """
    Initialize the extensions
    """
    mongo.init_app(app)
    redis_store.init_app(app)
    flask_bcrypt.init_app(app)
    # login_manager.init_app(app)

def create_app(config: Type[Config]):
    """
    Create the Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app

