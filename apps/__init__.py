
from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='radioX API',
          version='0.1',
          description='radioX API service for radioX'
          )

api.add_namespace(user_ns, path='/user')