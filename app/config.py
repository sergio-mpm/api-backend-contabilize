import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #####################################################
    #### Chave de acesso para API,
    #### a chave a seguir é uma chave somente 
    #### para exemplo/execucao da API.
    #####################################################
    JWT_SECRET_KEY = "52a91269896ba5df4e19a522eee0a0cb" 