from app.models.despesa import Despesa
from app.models.usuario import Usuario
from app.extensions import db
from datetime import datetime
from sqlalchemy import func

from app.schemas.despesa_schema import DespesaViewSchema

class DespesaService:
    def criar_despesa(self, data: dict) -> Despesa:
        if data["valor"] <= 0:
            raise ValueError("Valor Inválido")
        
        usuario = Usuario.query.get(data["cpf"])
        if not usuario:
            raise ValueError("Usuario não encontrado")
        
        despesa = Despesa(
            nome=data["nome"],
            valor=data["valor"],
            tipo=data["tipo"],
            data_despesa=data["data_despesa"],
            comentario=data["comentario"],
            cpf=data["cpf"]
        )

        db.session.add(despesa)
        db.session.commit()

        return despesa

    def listar_despesas(self):
        return Despesa.query.all()
    
    def buscar_despesa(self, id: int):
        despesa = Despesa.query.get(id)
        if not despesa:
            raise ValueError("Despesa não encontrada")
        return despesa

    def listar_despesas_por_usuario(self, cpf: str):
        return Despesa.query.filter(Despesa.cpf==cpf).all()

    def listar_despesas_por_tipo(self, tipo: str):
        return Despesa.query.filter(Despesa.tipo==tipo).all()
    
    def lista_despesas_por_data(self, data_despesa: datetime):
        return Despesa.query.filter(Despesa.data_despesa==data_despesa).all()
    
    def listar_por_periodo(self, data_inicio: datetime, data_fim: datetime):
        return (Despesa.query.filter(Despesa.data_despesa.between(data_inicio, data_fim)).all())
    
    def excluir_despesa(self, id: int) -> None:
        despesa = Despesa.query.get(id)
        if not despesa:
            raise ValueError("Despesa não encontrada")
        
        db.session.delete(despesa)
        db.session.commit()
        
    def serializar_nome_responsavel_despesa(self, despesas: list[Despesa]):
        lista_view_despesas = list[DespesaViewSchema]
        for despesa in despesas:
            usuario = Usuario.query.get(despesa.cpf)
            despesa_view = DespesaViewSchema (
                id = despesa.id,
                nome = despesa.nome,
                valor = despesa.valor,
                tipo = despesa.tipo,
                data_despesa = despesa.data_despesa,
                comentario = despesa.comentario,
                responsavel = usuario.nome if usuario else None
            )
            lista_view_despesas.append(despesa_view)
        
        return lista_view_despesas
            

    def atualiza_despesa(self, id: int, data: dict) -> Despesa:
        despesa = Despesa.query.get(id)
        if not despesa:
            raise ValueError("Despesa não encontrada")
        
        if "nome" in data:
            if data["nome"] is None:
                raise ValueError("Despesa precisa de um nome")
            despesa.nome = data["nome"]
        
        if "valor" in data:
            if data["valor"] <= 0:
                raise ValueError("Valor não pode ser zero")
            despesa.valor = data["valor"]

        if "tipo" in data:
            despesa.tipo = data["tipo"]
        
        if "data_despesa" in data:
            despesa.data_despesa = data["data_despesa"]
        
        if "cpf" in data:
            if data["cpf"] is None or "":
                raise ValueError("CPF não pode ser zerado")
            despesa.cpf = data["cpf"]

        db.session.commit()
        return despesa
    
    def calcula_despesas_totais(self) -> float:
        despesasTotais = (
            db.session.query(func.sum(Despesa.valor))
            .scalar()
        )
        #Se não houverem despesas retornaremos zero
        return despesasTotais or 0.0
        
    def calcula_despesas_totais_por_usuario(self, cpf: int) -> float:
        despesasTotais = (
            db.session.query(func.sum(Despesa.valor))
            .filter(Despesa.cpf == cpf)
            .scalar()
        )
        #Retorna despesas totais por cada usuário
        return despesasTotais or 0.0

    def calcula_despesas_totais_por_tipo(self, tipo: str) -> float:
        despesasTotais = (
            db.session.query(func.sum(Despesa.valor))
            .filter(Despesa.tipo == tipo)
            .scalar()
        )
        #Retorna despesas totais por tipo
        return despesasTotais or 0.0
    
    def calcula_despesas_totais_por_periodo(self, inicio, fim) -> float:
        despesasTotaisPeriodo = (
            db.session.query(func.sum(Despesa.valor))
            .filter(Despesa.data_despesa.between(inicio,fim))
            .scalar()
        )
        #Retorna despesas totais por periodo
        return despesasTotaisPeriodo or 0.0
    