from typing import Dict,Tuple

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
            auth_token = data
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, str):
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