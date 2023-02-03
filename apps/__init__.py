
from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='radioX_v0.1',
          version='0.1',
          description='radioX_v0.1 API service for radioX'
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
