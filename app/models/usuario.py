from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import base

class Usuario(base):
    __tablename__ = 'usuarios'

    cpf = Column("pk_usuario", Integer, primary_key=True, nullable=False)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    data_nascimento = Column(DateTime)

    despesas = relationship(
        "Despesas",
        back_populates="responsavel",
        cascade="all, delete-orphan"
    )


    def __init__(self, cpf:int, nome:str, email:str, data_nascimento:DateTime):
        """
            instancia um usuario no sistema

            Arguments:
                Cpf: cpf da pessoa e identificados unico no sistema
                nome: nome do usuario
                email: email do usuario no sistema
                data_nascimento: data de nascimento do usuario para identificar idade
        """
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento