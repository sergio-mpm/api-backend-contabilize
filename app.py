from flask import Flask, jsonify, request, redirect
from flask_openapi3 import openapi, Info, Tag
from flask_cors import CORS

from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from app.schemas import *
from app import create_app

info = Info(title="ContabilizeAPI", version="1.0.0")
app = openapi(__name__, info=info)
CORS(app)

#TAGS
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuario", description="Adição, visualização e associação de usuários a despesas à base")
despesa_tag = Tag(name="despesa", description="Adição, remoção e atualização de despesas à base")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')
