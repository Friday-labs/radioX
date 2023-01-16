'''
*** User Model***
'''
from pydantic import BaseModel,Field, EmailStr
from flask.json import jsonify
from datetime import datetime
from flask_jwt_extended import create_access_token,create_refresh_token
from apps.main.model.blacklist_token import BlacklistToken
from typing import List, Optional,Tuple

from .objectid import PydanticObjectId

class User(BaseModel):
    """ User Model for storing user related details """
    id: Optional[PydanticObjectId] = str(Field(None, alias="_id") )
    username: str
    email: EmailStr
    password : str

    def to_json(self):
        return jsonify(self.dict()) 

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        return data
    
    @staticmethod
    def encode_auth_token(self, user_id: int) -> Tuple:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            access_expires = datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5)
            refresh_expires = datetime.datetime.utcnow() + datetime.timedelta(days=10, seconds=5)
            access_token = create_access_token(identity=user_id, expires_delta=access_expires)
            refresh_token = create_refresh_token(identity=user_id, expires_delta=refresh_expires)
            return access_token,refresh_token
        except Exception as e:
            return e

