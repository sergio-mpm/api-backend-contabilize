from flask_openapi3 import APIBlueprint, Tag
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioDeleteSchema, UsuarioSchema, UsuarioUpdateSchema, UsuarioViewSchema


usuario_tag = Tag(
    name="Usuario",
    description="Operações de registros, atualizações e exclusões de usuários"
)


usuario_bp = APIBlueprint(
    "usuario",
    __name__,
    url_prefix="/usuario",
    tags=[usuario_tag]
)


@usuario_bp.post(
    "",
    responses={"200": UsuarioViewSchema, "400": dict}
)
def adiciona_usuario(body: UsuarioSchema):
    usuario = Usuario(**body.model_dump())

    try:
        db.session.add(usuario)
        db.session.commit()
        return usuario, 200
    
    except IntegrityError:
        db.session.rollback()
        return {"message":"Usuario já cadastrado"}, 400


@usuario_bp.put(
        "/<int:cpf>",
        tags=[usuario_tag],
        responses={200: UsuarioViewSchema, 404: dict}
)
def update_usuario(path: UsuarioDeleteSchema, form: UsuarioUpdateSchema):
    usuario = Usuario.query.filter_by(cpf=path.cpf).first()
    if not usuario:
        return {"message": "Usuário não encontrado"}, 404
    
    for campo, valor in form.model_dump(exclude_unset=True).Items():
        setattr(usuario, campo, valor)

    db.session.commit()
    return UsuarioViewSchema.model_validate(usuario).model_dump(), 200


@usuario_bp.delete(
    "/<int:cpf>",
    tags=[usuario_tag],
    responses={200: dict, 404: dict}
)
def delete_usuario(path: UsuarioDeleteSchema):
    usuario = Usuario.query.filter_by(cpf=path.cpf).first()
    if not usuario:
        return {"message": "Usuário não encontrado"}, 404
    
    db.session.delete(usuario)
    db.session.commit()
    return {"message": "Usuário removido com sucesso"}, 200


@usuario_bp.get(
    "/<int:cpf>",
    tags=[usuario_tag],
    responses={200: UsuarioViewSchema, 404: dict}
)
def get_usuario(path: UsuarioDeleteSchema):
    usuario = Usuario.query.filter_by(cpf=path.cpf).first()
    if not usuario:
        return {"message": "Usuário não encontrado"}, 404
    
    return (
        UsuarioViewSchema
        .model_validate(usuario)
        .model_dump(),
        200
    )


@usuario_bp.get(
    "",
    tags=[usuario_tag],
    responses={200: list[UsuarioViewSchema]}
)
def get_usuarios():
    usuarios = Usuario.query.all()
    return [
        UsuarioViewSchema.model_validate(u).model_dump()
        for u in usuarios
    ], 200