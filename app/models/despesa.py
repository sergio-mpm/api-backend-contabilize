from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import base, usuario

class Despesa(base):
    __tablename__ = 'despesas'

    id = Column("pk_despesa", Integer, primary_key=True, nullable=False)
    nome = Column(String(150), nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String(50), nullable=False)
    data_despesa = Column(DateTime, default=datetime.now())
    comentario = Column(String(255), nullable=True)

    cpf_responsavel = Column(
        Integer,
        ForeignKey("usuarios.cpf"),
        unique=True,
        nullable=False
    )

    responsavel = relationship("Usuario", back_populates="despesas")

    def __init__(self, id:int, nome:str, valor:float, tipo:str, comentario:str, cpf_responsavel:int, data_despesa:Union[DateTime, None] = None):
        """
            Insere o registro de uma despesa realizada
        """

        self.id = id
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
        self.comentario = comentario
        self.cpf_responsavel = cpf_responsavel

        if data_despesa:
            self.data_despesa = data_despesa
