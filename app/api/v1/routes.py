from flask import Blueprint
from flask_restful import Api

from app.api.v1.question.views import blogsView,blogView,update_blog,update_title,del_blog

VERSION_ONE = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_ONE)
API.add_resource(blogsView, '/questions')
API.add_resource(blogView, '/questions/<int:blog_id>')
API.add_resource(update_blog, '/questions/<int:blog_id>/blog')
API.add_resource(update_title, '/questions/<int:blog_id>/title')
API.add_resource(del_blog, '/questions/<int:blog_id>')

