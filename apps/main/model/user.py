'''
*** User Model***
'''
from pydantic import BaseModel,Field, EmailStr
from flask.json import jsonify
from typing import List, Optional, Union

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

class TokenModel(BaseModel):
    token :str