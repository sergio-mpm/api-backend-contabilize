from flask_openapi3 import APIBlueprint, Tag
from datetime import datetime

from app.services.despesa_service import DespesaService
from app.schemas.despesa_schema import (
    DespesaSchema,
    DespesaUpdateSchema,
    DespesaViewSchema,
    DespesaBuscaSchema,
    ListagemDespesasSchema
)


despesa_tag = Tag(
    name="Despesa",
    description="Operações de registros, consultas, atualizações e exclusões de despesas."
)

despesa_bp = APIBlueprint(
    "despesas",
    __name__,
    url_prefix="/despesas",
    tags=[despesa_tag]
)

service = DespesaService()


# =========================
# CRIAR DESPESA
# =========================
@despesa_bp.post(
    "",
    responses={200: DespesaViewSchema, 400: dict}
)
def criar_despesa(body: DespesaSchema):
    """
    Cria uma nova despesa
    """
    try:
        despesa = service.criar_despesa(body.model_dump())
        return despesa, 201
    except ValueError as e:
        return {"message": str(e)}, 400


# =========================
# LISTAR TODAS
# =========================
@despesa_bp.get(
    "",
    responses={200: ListagemDespesasSchema}
)
def listar_despesas():
    """
    Lista todas as despesas
    """
    despesas = service.listar_despesas()
    return {"despesas": despesas}, 200


# =========================
# BUSCAR POR ID
# =========================
@despesa_bp.get(
    "/<int:id>",
    responses={200: DespesaViewSchema, 404: dict}
)
def buscar_despesa(path: DespesaBuscaSchema):
    """
    Retorna uma despesa pelo ID
    """
    try:
        despesa = service.buscar_despesa(path.id)
        return despesa, 200
    except StopIteration:
        return {"message": "Despesa não encontrada"}, 404


# =========================
# ATUALIZAR DESPESA
# =========================
@despesa_bp.put(
    "/<int:id>",
    responses={200: DespesaViewSchema, 404: dict}
)
def atualizar_despesa(path: DespesaBuscaSchema, body: DespesaUpdateSchema):
    """
    Atualiza uma despesa parcialmente
    """
    try:
        despesa = service.atualiza_despesa(
            path.id,
            body.model_dump(exclude_unset=True)
        )
        return despesa, 200
    except ValueError as e:
        return {"message": str(e)}, 404


# =========================
# EXCLUIR DESPESA
# =========================
@despesa_bp.delete(
    "/<int:id>",
    responses={204: None, 404: dict}
)
def excluir_despesa(path: DespesaBuscaSchema):
    """
    Exclui uma despesa
    """
    try:
        service.excluir_despesa(path.id)
        return "", 204
    except ValueError as e:
        return {"message": str(e)}, 404


# =========================
# TOTAIS
# =========================
@despesa_bp.get("/total")
def total_despesas():
    """
    Retorna o valor total das despesas
    """
    return {"total": service.calcula_despesas_totais()}, 200


@despesa_bp.get("/total/usuario/<int:cpf>")
def total_por_usuario(path):
    """
    Total de despesas por usuário
    """
    return {
        "cpf": path.cpf,
        "total": service.calcula_despesas_totais_por_usuario(path.cpf)
    }, 200


@despesa_bp.get("/total/tipo/<string:tipo>")
def total_por_tipo(path):
    """
    Total de despesas por tipo
    """
    return {
        "tipo": path.tipo,
        "total": service.calcula_despesas_totais_por_tipo(path.tipo)
    }, 200
