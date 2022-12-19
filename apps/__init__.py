from  flask import Flask
from flask_login import LoginManager
from importlib import import_module
from flask_pymongo import PyMongo

mongo = PyMongo()
login_manager = LoginManager()


def register_extensions(app):
    mongo.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('main'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app

