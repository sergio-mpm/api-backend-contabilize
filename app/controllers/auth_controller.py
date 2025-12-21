from flask_openapi3 import APIBlueprint, Tag
from flask_jwt_extended import create_access_token
from app.services.usuario_service import UsuarioService

from app.schemas.auth_schema import AuthSchema, TokenSchema

auth_tag = Tag(
    name="Authenticator",
    description="Operação de autenticação de usuários na aplicação."
)

auth_bp = APIBlueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    abp_tags=[auth_tag]
)

service_usuario = UsuarioService()


@auth_bp.post(
        "/login",
        summary="Login de usuário",
        responses={200: TokenSchema}
)
def login(body: AuthSchema):
    """
    Login do usuário (CPF)
    """
    usuario = service_usuario.obter_usuario(body.cpf)
    token = create_access_token(identity=usuario.cpf)
    return {"access_token": token}, 200
