import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource

from app.api.validators import parser,parser_edit_blog,parser_edit_title

blogs = []

class myDatabase(Resource):
    def __init__(self):
        self.db = blogs

        if len(self.db) == 0:
            self.id = 1
        else:
            self.id = len(self.db) + 1

    
    def post_blog(self):
        parser.parse_args()
        data = {
            'id': self.id,
            'title': request.json.get('title'),
            'blog':request.json.get('blog'),
            'dateposted': datetime.datetime.utcnow()            
            }
        self.db.append(data)
        return self.id

    def get_blogs(self):
        return self.db

    def get_single_blog(self,blog_id):
        for blog in self.db:
            if blog['id'] == blog_id:
                return blog
        return "blog does not exist"

    def update_sinle_blog(self,blog): 
        parser_edit_blog.parse_args()       
        blog['blog'] = request.json.get('blog')
        return "updated"

    def update_blog_title(self,title):
        parser_edit_title.parse_args()
        title['title'] = request.json.get('title')
        return "updated"

    def delete_blog(self,blog):
        self.db.remove(blog)
        return "deleted"


