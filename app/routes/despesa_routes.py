from flask_openapi3 import APIBlueprint, Tag
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models.despesa import Despesa
from app.schemas.despesa import DespesaBuscaSchema, DespesaSchema, DespesaDeleteSchema, DespesaUpdateSchema, DespesaViewSchema, ListagemDespesasSchema


despesa_tag = Tag(
    name="Despesa",
    description="Operações de registros, atualizações e exclusões de despesas realizadas."
)


despesa_bp = APIBlueprint(
    "despesa",
    __name__,
    url_prefix="/despesa",
    tags=[despesa_tag]
)


@despesa_bp.post(
    "",
    responses={"200": DespesaViewSchema, "400": dict}
)
def adiciona_despesa(body: DespesaSchema):
    despesa=Despesa(**body.model_dump())

    try:
        db.session.add(despesa)
        db.session.commit()
        return despesa, 200
    
    except IntegrityError:
        db.session.rollback()
        return {"message": "Despesa já cadastrada"}, 400
    

@despesa_bp.put(
    "/<int:id>",
    tags=[despesa_tag],
    responses={200: DespesaViewSchema, 404: dict}
)
def update_despesa(path: DespesaBuscaSchema, form: DespesaUpdateSchema):
    despesa = Despesa.query.filter_by(id=path.id).first()
    if not despesa:
        return {"message": "Despesa não encontrada"}, 404
    
    for campo, valor in form.model_dump(exclude_unset=True).Items():
        setattr(despesa, campo, valor)

    db.session.commit()
    return DespesaViewSchema.model_validate(despesa).model_dump(), 200


@despesa_bp.get(
    "/<int:id>",
    tags=[despesa_tag],
    responses={200: DespesaViewSchema, 404: dict}
)
def get_despesa(path: DespesaViewSchema):
    despesa = Despesa.query.filter_by(id=path.id).first()
    if not despesa:
        return {"message": "Despesa não encontrada no cadastro"}, 404
    
    return(
        DespesaViewSchema
        .model_validate(despesa)
        .model_dump(),
        200
    )


@despesa_bp.get(
    "",
    tags=[despesa_tag],
    responses={200: list[DespesaViewSchema]}
)
def get_despesas():
    despesas = Despesa.query.all()
    return [
        DespesaViewSchema.model_validate(d).model_dump()
        for d in despesas
    ], 200