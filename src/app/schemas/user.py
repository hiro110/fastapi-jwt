from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: Optional[str] = None


class UserInDB(User):
    hashed_password: str
