from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy import DateTime
from models.usuario import Usuario

from schemas import DespesaSchema

class UsuarioSchema(BaseModel):
    cpf: int = "12345678900"
    nome: str = "João da Silva"
    email: str = "seuemail@email.com.br"
    data_nascimento: DateTime = "01/02/1991"


class UsuarioBuscaSchema(BaseModel):
    cpf: int = "12345678900"


class ListagemUsuariosSchema(BaseModel):
    usuarios: List[UsuarioSchema]


class UsuarioViewSchema(BaseModel):
    cpf: int = "12345678900"
    nome: str = "João da Silva"
    email: str = "seuemail@email.com.br"


def apresenta_usuario(usuarios: List[Usuario]):
    result = []
    for usuario in usuarios:
        result.append({
            "cpf": usuario.cpf,
            "nome": usuario.nome
        })

    return {"usuarios": result}


class UsuarioDeleteSchema(BaseModel):
    cpf: int = "12345678900"
    nome: str = "João da Silva"