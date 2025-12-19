from pydantic import BaseModel
from typing import Optional, List
from marshmallow import Schema, fields
from datetime import datetime

from ..models.despesa import Despesa

from app.schemas import usuario_schema


class DespesaSchema(BaseModel):
    nome: str
    valor: float
    tipo: str
    data_despesa: datetime = datetime.now


class DespesaBuscaSchema(BaseModel):
    id: int = 1


class ListagemDespesasSchema(BaseModel):
    despesas: List[DespesaSchema]


class UsuarioTotalPathSchema(BaseModel):
    cpf: str


class TipoTotalPathSchema(BaseModel):
    tipo: str


class DespesaViewSchema(BaseModel):
    id: int
    nome: str
    valor: float
    tipo: str
    data_despesa: datetime
    comentario: str | None = None
    responsavel: str | None = None


class DespesaViewUsuarioTotalSchema(BaseModel):
    cpf: str
    total: float


class DespesaViewTipoTotalSchema(BaseModel):
    typo: str
    total: float


def apresenta_despesas(despesas: List[Despesa]) -> dict:
    return {
        "despesas": [
            {
                "id": d.id,
                "nome": d.nome,
                "valor": d.valor,
                "tipo": d.tipo,
                "data_despesa": d.data_despesa,
                "comentario": getattr(d, "comentario", None),
                "responsavel": getattr(d.responsavel, "nome", None)
            }
            for d in despesas
        ]
    }

def get_nome_responsavel(self, obj):
    return obj.responsavel.nome


class DespesaUpdateSchema(BaseModel):
    nome: str
    valor: float
    tipo: str
    data_despesa: datetime
    comentario: str | None = None
    responsavel: str | None = None


def apresenta_despesa(despesa: Despesa) -> dict:
    return {
        "id": despesa.id,
        "nome": despesa.nome,
        "valor": despesa.valor,
        "tipo": despesa.tipo,
        "data_despesa": despesa.data_despesa,
        "comentario": getattr(despesa, "comentario", None),
        "responsavel": getattr(despesa.responsavel, "nome", None)
    }
