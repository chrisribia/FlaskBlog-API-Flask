import datetime

import psycopg2.extras
from flask import request
from flask_restful import reqparse

from werkzeug.security import check_password_hash

from app.api.db_config import connection
from app.api.db_config import DATABASE_URL as url

from app.api.validators import  validate_string


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title',
                    type=validate_string,
                    required=True,
                    nullable=False,
                    trim=True,
                    help="This field cannot be left blank or should be properly formated"
                    )

parser.add_argument('description',
                    type=validate_string,
                    required=True,
                    nullable=False,
                    help="This field cannot be left blank or should be properly formated"
                    )

class BlogsModel:
    """class for manipulating user data"""

    def __init__(self):
        self.db = connection(url)

    def save(self, user_id):
        parser.parse_args()
        data = {
            'user_id': user_id,
            'title': request.json.get('title'),
            'description': request.json.get('description')
        }

        query = """INSERT INTO blogs (user_id,title, description) VALUES({0},'{1}','{2}');""".format(
             data['user_id'], data['title'], data['description'])
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return data['user_id']

    def get_all_blogs(self):
        query = """SELECT * FROM blogs """
        conn = self.db
        cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def get_single_blog(self,blog_id):
        query = """SELECT user_id,title,description FROM   blogs   WHERE blog_id = {0}""".format(blog_id)
        conn = self.db
        cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        results = cursor.fetchone()
        if results == None:
            return None
        return results
    
    def update_blog(self,blog_id):
        """method to update a single"""
        new_blog = request.json.get('description')
        query = """UPDATE blogs SET description = '{0}' WHERE blog_id = {1}""".format(new_blog,blog_id)
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return "updated"

    def delete_blog(self,blog_id):
        """method to delete a single blog"""
        query = """DELETE  FROM blogs WHERE blog_id = {0} """.format(blog_id)

        del_query = """DELETE FROM comments WHERE blog_id = {0}""".format(blog_id)

        conn = self.db
        cursor = conn.cursor()
        del_list = [query,del_query]
        
        for n in del_list:
            cursor.execute(n)
            conn.commit()       
        return "deleted"

    

    def save_comments(self,blog_id,user_id):
        #parser.parse_args()
        """method to save a comment"""
        comment = request.json.get('comment')
        query = """INSERT INTO comments (blog_id,user_id,comment) 
                VALUES({0},{1},'{2}')""".format(blog_id,user_id,comment)
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return "saved"


    def get_if_user_preferred(self,blog_id):
        """see if there is user preferred"""
        user_preferred = True
        query = """SELECT * FROM comments WHERE blog_id = {0} and user_preferred = '{1}'""".format(blog_id,user_preferred)
        conn = self.db
        cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        results = cursor.fetchall()
        total_com = cursor.rowcount
        cursor.close()
        n = str(total_com)        
        if results == None:
            return None
        return n

    def set_false_preferred(self,blog_id,comment_id):
        """set false to preferred user"""
        user_preferred  = False

        user_preferred1 = True

        query = """UPDATE comments SET user_preferred = '{0}' WHERE blog_id = {1} """.format(user_preferred,blog_id)

        query1 = """UPDATE comments SET user_preferred = '{0}' WHERE comment_id = {1}""".format(user_preferred1,comment_id)
       
        conn = self.db
        cursor = conn.cursor()
        queries = [query,query1]
        for x in queries:
            cursor.execute(x)
            cursor.commit()
        return "updated"

    def update_preferred(self,comment_id):
        """method to set new preferred user"""
        user_preferred = True
        query = """UPDATE comments SET user_preferred = '{0}' WHERE comment_id = {1} """.format(user_preferred,comment_id)
        conn = self.db
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.commit()
        return "updated"