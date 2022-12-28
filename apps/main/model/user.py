'''
*** User Model***
'''
from pydantic import BaseModel,Field
from flask.json import JSONEncoder
from typing import List, Optional, Union

from .objectid import PydanticObjectId

class User(BaseModel):
    """ User Model for storing user related details """
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    slug: str
    name: str
    email:str
    password : str

    def to_json(self):
        return JSONEncoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data["_id"] is None:
            data.pop("_id")
        return data