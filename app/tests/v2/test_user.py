import unittest
import json
import jwt
import datetime
import os

from ... import create_app
from app.api.db_config import create_tables
from app.tests.v2.user_data import test_user, user, data5, data6

secret = os.getenv('SECRET_KEY')

class UserTestCase(unittest.TestCase):
    """Class for Users testcase"""

    def setUp(self):
        """set up method initialising resused variables"""
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

        self.data = user
        self.data5 = data5
        self.data6 = data6

    def test_user_signup(self):
        """Test user signup"""
        response = self.app.post(
            "/api/v2/auth/signup", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_user_signin(self):
        """Test post a user signin"""
        self.app.post("/api/v2/auth/signup", headers={'Content-Type': 'application/json'},
                      data=json.dumps(self.data))

        response = self.app.post(
            "/api/v2/auth/signin", headers={'Content-Type': 'application/json'},
             data=json.dumps(dict(
                email='joe@gmail.com',
                password='123456'
            )))

        data = json.loads(response.data)        
        self.assertTrue(data['message'] == 'You have created an account you can now sign in')
        self.assertEqual(response.status_code, 201)

    def test_user_signin_wrong_password(self):
        """Test post a user signin"""
        self.app.post("/api/v2/auth/signup", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        response = self.app.post("/api/v2/auth/signin", headers=self.headers, data=json.dumps(self.data6))
        self.assertEqual(response.status_code, 404)
     
    def test_duplicate_user_name(self):
        """Test signup a user with existing username"""
        self.app.post("/api/v2/auth/signup", headers={'Content-Type': 'application/json'},
                      data=json.dumps(self.data))
        response = self.app.post(
            "/api/v2/auth/signup", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        result = json.loads(response.data)
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['error'], "username already taken please try another one")
    