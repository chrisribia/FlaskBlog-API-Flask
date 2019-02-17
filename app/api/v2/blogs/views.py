"""Views for posting blogs"""
from flask import jsonify, request
from flask_restful import Resource
from app.api.v2.blogs.models import BlogsModel
from app.api.v2.token_decorator import require_token
from app.api.v2.user.models import UserModel


class Blogs(Resource):
    """This class deals with posting and reading blogs"""

    def __init__(self):
        """
        executes when the class is being initiated
        used to assign values to object properties
        self parameter is a reference to tha class instance itself & is used 
        to access variables that belong to that class
        """
        self.db = BlogsModel()

    @require_token
    def post(current_user, self):
        """method for posting a blogs"""
        blog = self.db.save(current_user['user_id'])
        return jsonify({
            "status": 201,
            "data": blog,
            "message": "Created a blogs"
        })

    @require_token
    def get(current_user,self):
        """method from get all blogs"""
        get_blogs = self.db.get_all_blogs()
        return jsonify({
            "status": 201,
            "data" : get_blogs
        })
    
class Blog(Resource):
    """ class to deal with a single blog"""
    def __init__(self):
        """method to initialize class variables"""
        self.db = BlogsModel()

    @require_token
    def get(current_user,self,blog_id):
        """method to get a single blog"""
        get_blog = self.db.get_single_blog(blog_id)       
        if get_blog == None:
            return "the blog  doesn't exist"
            
        return jsonify({
            "status" : 200,
            "message" : get_blog
        })
class update_blog(Resource):
    """class to update a single blog"""

    def __init__(self):
        self.db = BlogsModel()

    @require_token  
    def patch(current_user,self,blog_id):
        """method to a single blog"""
        get_blog = self.db.get_single_blog(blog_id)
        if get_blog == None:
            return "the blog to be updated doesn't exist"
        if current_user['user_id'] != get_blog['user_id']:
            return "you have no update authority to on this blog"            

        update_results = self.db.update_blog(blog_id)
        return jsonify({
            "status" : 200,
            "message" : update_results
        })
class delete_blog(Resource):
    """method to delete a single blog"""
    def __init__(self):
        self.db = BlogsModel()

    @require_token
    def delete(current_user,self,blog_id):
        
        get_blog = self.db.get_single_blog(blog_id)
        if get_blog == None:
            return "no such blog "

        if current_user['user_id'] != get_blog['user_id']:
            return "you have no delete authority to on this blog"   

        """method to a sigle blog"""
        delete_results = self.db.delete_blog(blog_id)
        return jsonify({
            "status" : 200,
            "message" : delete_results          
        })

class save_comment(Resource):
    """module to save comment"""

    def __init__(self):
        self.db = BlogsModel()

    @require_token
    def post(current_user,self,blog_id):

        get_blog = self.db.get_single_blog(blog_id)
        if get_blog == None:
            return "no such blog "

        comment_save = self.db.save_comments(blog_id,current_user['user_id'])
        if comment_save != "saved":
            return "there is a problem"
        return jsonify({
            "status" : 200,
            "message" : comment_save

        })


class get_mycomments(Resource):
    """class to get all my comments"""
    
    def __init__(self):
        self.db = BlogsModel()

    @require_token
    def get(current_user,self,blog_id):
        """view comments to a blog"""
        results_blog = self.db1.get_single_blog(blog_id)

        results_comments = self.db.get_myComments(blog_id)
        if results_comments == None:
            return "No comments for the blog"

        
        return jsonify({
            "status" : 200,
            "blog title" : results_blog['title'],
            "description" : results_blog['description'],
            "message" : results_comments
        })
""" class set_preferred(Resource):
     
    def __init__(self):
        self.db = BlogsModel()

    @require_token
    def patch(current_user,self,) 
 """

        

