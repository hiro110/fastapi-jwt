from typing import Optional

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(Token):
    name: Optional[str] = None
