from datetime import datetime
from pydantic import BaseModel

class BlacklistedToken(BaseModel):
    token: str
    blacklisted_on: datetime
    expires_on: datetime

    class Config:
        orm_mode = True