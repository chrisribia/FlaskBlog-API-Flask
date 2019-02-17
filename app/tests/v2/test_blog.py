import datetime
import json
import os
import unittest
import jwt

from ... import create_app
from app.api.db_config import create_tables
from app.tests.v2.user_data import test_user, blog_data

secret = os.getenv('SECRET_KEY')

class BlogTestCase(unittest.TestCase):
    """
        This class represents the questions test cases
    """
    def setUp(self):
        APP = create_app(config_name="testing")
        APP.testing = True
        self.app = APP.test_client()
        create_tables()
         

        self.test_user = test_user

        payload = {
            "user_name": self.test_user['user_name'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        }

        token = jwt.encode(
            payload=payload, key=secret, algorithm='HS256')

        self.headers = {'Content-Type': 'application/json',
                        'token': token
                        }

        self.headers_invalid = {
            'Content-Type': 'application/json', 'token': 'Tokenmbaya'}
        self.blog = blog_data


    def test_get_all_questions_no_token(self):
        """method to test get all questions with no token"""
        response = self.app.get("/api/v2/blogs")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'], "Token is missing")  

    def test_post_blog(self):
        """Test post a  blog"""
        response = self.app.post(
            "/api/v2/blogs", headers=self.headers, data=json.dumps(self.blog))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 201)

    def test_delete_blog(self):
        """Test get a specific question"""
        self.app.post("/api/v2/blogs/1", headers=self.headers,
                      data=json.dumps(self.blog))
        response = self.app.delete("/api/v2/blogs/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_nonExistingBlog(self):
        """Test get a specific question"""
        self.app.post("/api/v2/blogs/1", headers=self.headers,
                      data=json.dumps(self.blog))
        response = self.app.delete("/api/v2/blogs/18", headers=self.headers)
        self.assertEqual(response.status_code, 200)