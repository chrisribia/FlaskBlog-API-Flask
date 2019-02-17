import datetime

import psycopg2.extras
from flask import request
from flask_restful import reqparse

from app.api.db_config import connection
from app.api.db_config import DATABASE_URL as url


class CommentsModel:
    def __init__(self):
        self.db = connection(url)

    def get_myComments(self,blog_id):
        """methods my comments to a blogs"""
        query = """SELECT comment_id,user_id,comment,user_preferred  FROM comments WHERE blog_id = {0}""".format(blog_id)
        conn = self.db
        cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        results = cursor.fetchall()
        total_com = cursor.rowcount
        n = str(total_com)
        
        if results == None:
            return None
        return results, " ","total comments "+ n

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