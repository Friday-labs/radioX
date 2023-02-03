from typing import Dict
from datetime import datetime
from apps.main import redis_store
from apps.main.model.blacklist_token import BlacklistedToken


def save_token(token: str) -> Dict[str, any]:
    BlacklistedToken(token=token).validate({'token':token})
    try:
        # insert the token with fields
        expired_on = datetime.utcnow()
        redis_store.set(token,expired_on.strftime("%m/%d/%Y, %H:%M:%S"))
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
        return response_object, 401