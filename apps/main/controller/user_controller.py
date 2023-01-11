from flask_restx import Resource

from ..utils.dto import UserDto
from ..service.auth.user_service import register_user

api = UserDto.api
_user = UserDto.user

# Define the route for the user resource
@api.route('/')
class Users(Resource):

    # Define the expected responses
    @api.response(201, 'User successfully created.')
    @api.response(400, 'Bad Request')
    # Define the route documentation
    @api.doc('create a new user')
    # Use the DTO to parse and validate the request payload
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        try:
            # Get the request payload from the API
            data = api.payload
            # Use the user service to handle the request
            return register_user(data=data)
        except Exception as e:
            # Return an error message and a 400 status code for any unexpected errors
            return {'message': str(e)}, 400