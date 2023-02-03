from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from apps.main.service.auth.auth_service import Auth
from ..utils.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
    User Login Resource
    """
    @api.doc('user login')
    @api.response(200, 'User successfully logged in.')
    @api.response(400, 'Bad Request')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    @api.response(200, 'User logged out.')
    @api.response(400, 'Bad Request')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)