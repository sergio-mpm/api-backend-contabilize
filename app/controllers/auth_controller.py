from flask_openapi3 import APIBlueprint
from flask_jwt_extended import create_access_token
from app.services.usuario_service import UsuarioService

auth_bp = APIBlueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    tags=["Auth"]
)

service = UsuarioService()


@auth_bp.post("/login")
def login(body: dict):
    """
    Login do usuário (CPF)
    """
    usuario = service.apresenta_usuario(body["cpf"])
    token = create_access_token(identity=usuario.cpf)
    return {"access_token": token}, 200
