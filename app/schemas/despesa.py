from pydantic import BaseModel
from typing import Optional, List
from marshmallow import Schema, fields

from sqlalchemy import DateTime
from models.despesa import Despesa

from schemas import usuario


class DespesaSchema(BaseModel):
    nome: str = "Compra Lanche"
    valor: float = "35.90"
    tipo: str = "variavel"
    data_despesa: DateTime = "11/11/2025"


class DespesaBuscaSchema(BaseModel):
    id: int = "001"


class ListagemDespesasSchema(BaseModel):
    despesas:List[DespesaSchema]


def apresenta_despesas(despesas: List[Despesa]):
    result = []
    for despesa in despesas:
        result.append({
            "nome": despesa.nome,
            "valor": despesa.valor,
            "tipo": despesa.tipo,
            "data_despesa": despesa.data_despesa
        })

    return {"despesa": result}


class DespesaViewSchema(BaseModel):
    id: int = "1"
    nome: str = "gasto xpto"
    valor: float = "35.90"
    tipo: str = "variavel"
    data_despesa: DateTime = "11/11/2025"
    comentario: str = "Gasto xpto feito via internet"
    responsavel: str = fields.Method("get_nome_responsavel")


def get_nome_responsavel(self, obj):
    return obj.responsavel.nome


class DespesaUpdateSchema(BaseModel):
    nome: str = "gasto xpto"
    valor: float = "35.90"
    tipo: str = "variavel"
    data_despesa: DateTime = "11/11/2025"
    comentario: str = "Gasto xpto feito via internet"
    responsavel: str = fields.Method("get_nome_responsavel")

class DespesaDeleteSchema(BaseModel):
    statusCode: int
    message: str
    nome: str


def apresenta_despesa(despesa: Despesa):
    return {
        "id": despesa.id,
        "nome": despesa.nome,
        "valor": despesa.valor,
        "tipo": despesa.tipo,
        "data_despesa": despesa.data_despesa,
        "responsavel": fields.Method("get_nome_responsavel")
    }