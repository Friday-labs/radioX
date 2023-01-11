from flask import request
from flask_restx import Resource
# from flask_pydantic import validate

from ..utils.dto import UserDto
from ..service.auth.user_service import register_new_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
# @validate()
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return register_new_user(data=data)