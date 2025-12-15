from flask import Flask, jsonify, request, redirect
from flask_openapi3 import openapi, Info, Tag
from flask_cors import CORS

from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from app.schemas import *
from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
