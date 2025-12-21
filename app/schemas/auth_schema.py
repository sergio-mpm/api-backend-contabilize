from pydantic import BaseModel
from typing import Optional, List

class AuthSchema(BaseModel):
    cpf: str = "12345678900"

class TokenSchema(BaseModel):
    access_token: str