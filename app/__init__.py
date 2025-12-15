from flask import Flask
from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate

def create_app():
    info = Info(title="ContabilizeAPI", version="1.0.0")
    app = OpenAPI(__name__, info=info)

    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    #importação de rotas para realização do migrate
    from app.models import despesa, usuario

    #registro de rotas
    from app.routes.despesa_routes import despesa_bp
    app.register_api(despesa_bp)

    return app