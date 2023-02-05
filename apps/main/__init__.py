'''
***
'''
from typing import Type
from flask import Flask
from flask_restx import Api
# from flask_login import LoginManager
from flask_redis import FlaskRedis
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from apps.main.config import Config

mongo = PyMongo()
jwt = JWTManager()
"""
We can create multiple pymongo instances for 
different database
"""
redis_store = FlaskRedis()


def register_extensions(app : Flask):
    """
    Initialize the extensions
    """
    mongo.init_app(app)
    jwt.init_app(app)
    redis_store.init_app(app)

def create_app(config: Type[Config]):
    """
    Create the Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app

