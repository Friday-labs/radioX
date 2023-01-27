from flask_restx import Namespace, fields

class UserDto:
    # Define the namespace for the user-related operations
    api = Namespace('user', description='user related operations')
    # Define the model for the user data
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        #'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    # logout_api = Namespace('logout', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    user_auth_token = api.model('auth_token', {
        'Authorization_token': fields.String(required=True, description='valid_auth_token'),
    })

   