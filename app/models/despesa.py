from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from ..extensions import db

from ..models import base, usuario

class Despesa(db.Model):
    __tablename__ = 'despesas'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    data_despesa = db.Column(db.Date, default=datetime.now)
    comentario = db.Column(db.String(255), nullable=True)

    cpf = Column(
        db.String(11),
        ForeignKey("usuarios.cpf"),
        nullable=False
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="despesas"
    )

    def __init__(self, nome:str, valor:float, tipo:str, comentario:str, cpf:str, data_despesa:Union[DateTime, None] = None):
        """
            Insere o registro de uma despesa realizada
        """

        self.nome = nome
        self.valor = valor
        self.tipo = tipo
        self.comentario = comentario
        self.cpf = cpf

        if data_despesa:
            self.data_despesa = data_despesa

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": self.valor,
            "tipo": self.tipo,
            "data_despesa": self.data_despesa,
            "comentario": self.comentario,
            "cpf": self.cpf
        }
