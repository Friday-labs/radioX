from datetime import datetime
from pydantic import BaseModel
from apps.main import redis_store

class BlacklistedToken(BaseModel):
    token: str

    class Config:
        orm_mode = True

    @staticmethod
    def check_blacklist(auth_token: str) -> bool:
        # check whether auth token has been blacklisted
        if redis_store.exists(auth_token):
            return True
        else:
            return False