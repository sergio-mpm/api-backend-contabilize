from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy import DateTime
from ..models.usuario import Usuario

from ..schemas import despesa_schema
from datetime import datetime

class UsuarioSchema(BaseModel):
    cpf: str = "12345678900"
    nome: str = "João da Silva"
    email: str = "seuemail@email.com.br"
    data_nascimento: datetime = "1991-09-01"
    
    model_config = {
        "from_attributes": True
    }


class UsuarioBuscaSchema(BaseModel):
    cpf: str = "12345678900"


class UsuarioViewSchema(BaseModel):
    cpf: str = "12345678900"
    nome: str = "João da Silva"
    email: str = "seuemail@email.com.br"
    
    model_config = {
        "from_attributes": True
    }


class ListagemUsuariosSchema(BaseModel):
    usuarios: List[UsuarioSchema]


def apresenta_usuario(usuarios: List[Usuario]):
    result = []
    for usuario in usuarios:
        result.append({
            "cpf": usuario.cpf,
            "nome": usuario.nome
        })

    return {"usuarios": result}


class UsuarioDeleteSchema(BaseModel):
    cpf: str = "12345678900"
    nome: str = "João da Silva"


class UsuarioUpdateSchema(BaseModel):
    cpf: str = "12345678900"
    nome: str = "João da Silva"
    email: str = "seuemail@email.com.br"
    data_nascimento: datetime = "1993-09-24"
