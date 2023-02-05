from typing import Dict,Tuple
import time
from flask_jwt_extended import create_access_token

from apps.main import mongo
from apps.main.utils.password import verify_pass
from .blacklist_service import save_token
from ...model.user import User

class Auth:
    @staticmethod
    def login_user(data: Dict) -> Tuple[Dict, int]:
        try:
            # fetch the user data
            user = mongo.db.users.find_one({'email': data.get('email')})
            if user and verify_pass(data['password'],user['password']): ##Verify password
                auth_token = User.encode_auth_token(user_id=str(user['_id']))
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1] # 'Bearer eyasdczzx5eb7cf5a86d9755df3a6c593' 
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, dict):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def generate_tokens(data:str):
        if data:
            refresh_token = data.split(" ")[1]
        else:
            refresh_token = ''
        if refresh_token:
             # check if the refresh token exists and is valid
            is_valid = User.decode_auth_token(refresh_token)
            if isinstance(is_valid, dict):
            # get the user associated with the refresh token
                user_id = is_valid['sub']
                expiration_time = is_valid['exp']
                current_time = time.time()
                time_difference = expiration_time - current_time # In seconds
                if time_difference <=120:
                    return User.encode_auth_token(user_id)    
                else: 
                    # generate a new access token for the user
                    access_token = create_access_token(identity=user_id)
                    refresh_token = ''
                    # update the refresh token for the user
                    return access_token,refresh_token
            else:
                response_object = {
                    'status': 'fail',
                    'message': is_valid
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Refresh token has expired. Please log in again.'
            }
            return response_object, 403