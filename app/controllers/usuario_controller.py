from flask_openapi3 import APIBlueprint, Tag

from app.services.usuario_service import UsuarioService
from app.schemas.error_schema import ErrorSchema
from app.schemas.usuario_schema import (
    ListagemUsuariosSchema,
    UsuarioSchema,
    UsuarioUpdateSchema,
    UsuarioViewSchema,
    UsuarioBuscaSchema
)


usuario_tag = Tag(
    name="Usuario",
    description="Operações de registros, consultas, atualizações e exclusões de usuários"
)

usuario_bp = APIBlueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios",
    abp_tags=[usuario_tag]
)

service = UsuarioService()


# =========================
# CRIAR USUÁRIO
# =========================
@usuario_bp.post(
    "",
    responses={201: UsuarioViewSchema, 400: ErrorSchema}
)
def cadastrar_usuario(body: UsuarioSchema):
    """
    Cadastra um novo usuário
    """
    try:
        usuario = service.cadastra_usuario(body.model_dump())
        return usuario, 201
    except ValueError as e:
        return {"message": str(e)}, 400


# =========================
# LISTAR USUÁRIOS
# =========================
@usuario_bp.get(
    "",
    responses={200: ListagemUsuariosSchema}
)
def listar_usuarios():
    """
    Lista todos os usuários
    """
    return service.listar_usuarios(), 200


# =========================
# BUSCAR USUÁRIO POR CPF
# =========================
@usuario_bp.get(
    "/<int:cpf>",
    responses={200: UsuarioViewSchema, 404: ErrorSchema}
)
def apresentar_usuario(path: UsuarioBuscaSchema):
    """
    Retorna um usuário pelo CPF
    """
    try:
        usuario = service.apresenta_usuario(path.cpf)
        return usuario, 200
    except ValueError as e:
        return {"message": str(e)}, 404


# =========================
# ATUALIZAR USUÁRIO
# =========================
@usuario_bp.put(
    "/<int:cpf>",
    responses={200: UsuarioViewSchema, 404: ErrorSchema}
)
def atualizar_usuario(path: UsuarioBuscaSchema, body: UsuarioUpdateSchema):
    """
    Atualiza parcialmente um usuário
    """
    try:
        usuario = service.atualiza_cadastro_usuario(
            path.cpf,
            body.model_dump(exclude_unset=True)
        )
        return usuario, 200
    except ValueError as e:
        return {"message": str(e)}, 404


# =========================
# EXCLUIR USUÁRIO
# =========================
@usuario_bp.delete(
    "/<int:cpf>",
    responses={204: None, 404: ErrorSchema}
)
def excluir_usuario(path: UsuarioBuscaSchema):
    """
    Exclui um usuário
    """
    try:
        service.exclui_usuario(path.cpf)
        return "", 204
    except ValueError as e:
        return {"message": str(e)}, 404
