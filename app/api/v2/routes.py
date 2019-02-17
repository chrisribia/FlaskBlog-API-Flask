from flask import Blueprint
from flask_restful import Api

from app.api.v2.user.views import UserSignUp,UserSignIn
from app.api.v2.comments.views import commets_view,preferred_user
from app.api.v2.blogs.views import Blogs,Blog,update_blog,delete_blog,save_comment,get_mycomments

VERSION_DOS = Blueprint('apiv2', __name__, url_prefix='/api/v2')
API = Api(VERSION_DOS)

API.add_resource(UserSignUp, '/auth/signup')
API.add_resource(UserSignIn, '/auth/signIn')
API.add_resource(Blogs, '/blogs')
API.add_resource(Blog, '/blogs/<int:blog_id>')
API.add_resource(update_blog, '/blogs/<int:blog_id>/description')
API.add_resource(delete_blog, '/blogs/<int:blog_id>')
API.add_resource(save_comment, '/blogs/<int:blog_id>/comment')

#API.add_resource(save_comment, '/blogs/<int:blog_id>/comment/<int:comment_id>')
API.add_resource(commets_view, '/comments/<int:blog_id>')
#API.add_resource(preferred_user, '/comments/<int:blog_id>/<int:comment_id>')