from datetime import datetime
from typing import Dict ,Tuple
from pydantic import ValidationError
# from . import users
from apps.main import mongo#flask_bcrypt
from apps.main.utils.password import hash_pass,verify_pass
from ...model.objectid import PydanticObjectId
from ...model.user import User


def register_user(data: Dict) -> Tuple[Dict, int]:
    """
    Register a new user
    
    :param data: A dictionary containing the user's details
    :return: A tuple containing the response object and the HTTP status code
    """
    try:
        # Create an instance of the User model and validate the fields
        User(**data).validate(data)
         # Check if the user already exists in the database
        user = mongo.db.users.find_one({"email":data['email']})
        if not user:
            hashed_password = hash_pass(data['password'])
            data['password'] = hashed_password
            data["registered_on"]=datetime.utcnow()
             # insert the user into the database
            result = mongo.db.users.insert_one(data)
            # set the ID of the user model to the inserted ID
            # new_user.id = str(PydanticObjectId(result.inserted_id))
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            # return an error message and a 409 status code if the user already exists
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409
    except ValidationError as v_err:
        # return the validation errors and a 400 status code
        return {"error":v_err.errors()}, 400
    except Exception as e:
        # return an error message and a 500 status code for any unexpected errors
        return {"error":str(e)}, 500