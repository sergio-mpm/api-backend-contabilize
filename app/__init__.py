from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate

def create_app():
    info = Info(
        title="ContabilizeAPI",
        version="1.0.0",
        description="API para controle de despesas, registradas por usuarios diversos"
    )
    app = OpenAPI(__name__, info=info)

    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    #importação de rotas para realização do migrate
    from app.models import despesa, usuario

    #registro de rotas
    from app.controllers.despesa_controller import despesa_bp
    from app.controllers.usuario_controller import usuario_bp
    app.register_api(despesa_bp)
    app.register_api(usuario_bp)

    return app
