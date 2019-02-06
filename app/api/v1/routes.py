from flask import Blueprint
from flask_restful import Api

from app.api.v1.question.views import hello

VERSION_ONE = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_ONE)
API.add_resource(hello, '/questions')