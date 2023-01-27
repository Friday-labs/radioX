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