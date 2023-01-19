'''
*** User Model***
'''
from pydantic import BaseModel,Field, EmailStr
from flask.json import jsonify
from datetime import datetime
from flask_jwt_extended import create_access_token,create_refresh_token,decode_token
from typing import Optional,Tuple,Union

from apps.main.model.blacklist_token import BlacklistedToken
from .objectid import PydanticObjectId

class User(BaseModel):
    """ User Model for storing user related details """
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    username: str
    email: EmailStr
    password : str
    registered_on : Optional[datetime]

    def to_json(self):
        return jsonify(self.dict()) 

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        return data
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    
    @classmethod
    def update(cls, instance, **kwargs):
        data = instance.dict()
        data.update(kwargs)
        return cls(**data)
    
    @staticmethod
    def encode_auth_token(self, user_id: int) -> Tuple:
        """
        Generates the Auth Token
        :return: tuple
        """
        try:
            access_expires = datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5)
            refresh_expires = datetime.datetime.utcnow() + datetime.timedelta(days=10, seconds=5)
            access_token = create_access_token(identity=user_id, expires_delta=access_expires)
            refresh_token = create_refresh_token(identity=user_id, expires_delta=refresh_expires)
            return access_token,refresh_token
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[int, str]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = decode_token(auth_token)
            is_blacklisted_token = BlacklistedToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token Expired. Please log in again.'
            else:
                return payload['identity']
        except Exception as e:
            return str(e)