from app.models.despesa import Despesa
from app.models.usuario import Usuario
from app.schemas.despesa_schema import DespesaSchema, DespesaViewSchema
from app.schemas.usuario_schema import UsuarioSchema, UsuarioViewSchema
from app.services.despesa_service import DespesaService
from app.services.usuario_service import UsuarioService

service_despesa = DespesaService()
service_usuario = UsuarioService()

class AuthService:
    def autorizar_despesa(self, cpf: str, token: str) -> bool:
        if(cpf != token):
            return False
        else:
            return True

    def autorizar_login(self, cpf: str, token: str) -> bool:
        if(cpf != token):
            return False
        else:
            return True
        
    def autorizar_atualizar_despesa(self, id_despesa: int, token: str) -> bool:
        despesa = service_despesa.buscar_despesa(id_despesa)
        if(despesa.cpf != token):
            return False
        else:
            return True
        
    def autorizar_remover_despesa(self, id_despesa: int, token: str) -> bool:
        despesa = service_despesa.buscar_despesa(id_despesa)
        if(despesa.cpf != token):
            return False
        else:
            return True

    def autorizar_remover_usuario(self, cpf: str, token: str) -> bool:
        if(cpf != token):
            return False
        else:
            return True