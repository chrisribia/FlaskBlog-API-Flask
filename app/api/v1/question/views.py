from flask import jsonify,make_response,request
from flask_restful import Resource
from .modules import myDatabase


def blog_nonexistance():
    make_response(jsonify({
        "status" : 200,
        "message" : "blog does not exist"
    }),404)
class blogsView(Resource):

    def __init__(self):
        self.db = myDatabase()  

    def post(self):
        question = self.db.post_blog()
        return make_response(jsonify({
            "status" : 200,
            "message" : question
            }),201)

    def get(self):        
        blogs =  self.db.get_blogs()
        return make_response(jsonify({
            "status" : 200,
            "message" : blogs
            }),201)

class blogView(Resource):
    def __init__(self):
        self.db = myDatabase()
    
    def get(self,blog_id):
        the_blog = self.db.get_single_blog(blog_id)
        return make_response(jsonify({
            "status" : 200,
            "message" : the_blog
        }),201)


class update_blog(Resource):
    def __init__(self):
        self.db = myDatabase()

    def patch(self,blog_id):
        search_blog = self.db.get_single_blog(blog_id)
        if search_blog == "blog does not exist":
            return blog_nonexistance()

        new_blog = self.db.update_sinle_blog(search_blog)
        return make_response(jsonify({
            "status" : 404,
            "message" : new_blog

        }),201)

class update_title(Resource):
    def __init__(self):
        self.db = myDatabase()

    def patch(self,blog_id):
        search_blog = self.db.get_single_blog(blog_id)

        if search_blog == "blog does not exist":
            return blog_nonexistance
        new_blog_title = self.db.update_blog_title(search_blog)
        return make_response(
            jsonify({
                "status" : 200,
                "message" : new_blog_title
            }),201
        )

class del_blog(Resource):
    def __init__(self):
        self.db = myDatabase()

    def delete(self,blog_id):
        search_blog = self.db.get_single_blog(blog_id)
        if search_blog == "blog does not exist":
            return blog_nonexistance
        remove_blog = self.db.delete_blog(search_blog)
        return make_response(
            jsonify({
                "status" : 200,
                "message" : remove_blog
            }),201)
        
