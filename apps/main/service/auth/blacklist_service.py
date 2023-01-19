from typing import Dict
from apps.main import redis_store
from apps.main.model.blacklist_token import BlacklistedToken


def save_token(token: str) -> Dict[str, any]:
    blacklist_token = BlacklistedToken(token=token).dict() # convert the token to dict
    try:
        # insert the token with fields
        redis_store.hmset(token, blacklist_token)
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 200