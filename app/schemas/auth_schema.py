from pydantic import BaseModel
from typing import Optional, List

class AuthSchema(BaseModel):
    cpf: str
    nome: str

class TokenSchema(BaseModel):
    access_token: str