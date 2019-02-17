"""Views for commets blogs"""
from flask import jsonify, request
from flask_restful import Resource
from app.api.v2.blogs.models import BlogsModel
from app.api.v2.token_decorator import require_token
from app.api.v2.comments.models import CommentsModel

class commets_view(Resource):
    def __init__(self):
        """
        executes when the class is being initiated
        used to assign values to object properties
        self parameter is a reference to tha class instance itself & is used 
        to access variables that belong to that class
        """
        self.db = CommentsModel()
        self.db1 = BlogsModel()

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

class preferred_user(Resource):

    @require_token
    def patch(current_user,self,blog_id,comment_id):
        """accept a comment"""
        """ 
        owner = self.db1.get_single_blog(blog_id)
        if current_user['user_id'] != owner['user_id']:
            return "you can't accept this comment"
        """
        confirm_isPreferred = self.db.get_if_user_preferred(blog_id)
        if confirm_isPreferred == None:
            results = self.db.update_preferred(blog_id)
            return results
        else:
            results = self.id.set_false_preferred(blog_id,current_user['user_id'])
            return results


