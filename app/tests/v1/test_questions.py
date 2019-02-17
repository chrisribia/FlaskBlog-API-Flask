
import json
import unittest
import datetime
from ... import create_app


class QuestionTestCase(unittest.TestCase):
    """
    This class represents the question test cases
    """

    def setUp(self):
        APP = create_app("testing")
        self.app = APP.test_client()

        self.blog = {
            "id": 1,
            "title": "How to write tests",
            "blog": "I was wondering  how do u write tests"
            

        }
    def test_post_blog(self):
        """method to test post a blog endpoint"""
        response = self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['status'], 200)


    def test_get_all_questions_list_empty(self):
        """method to test get all questions endpoints"""
        response = self.app.get("/api/v1/questions")
        self.assertEqual(response.status_code, 201)

    def test_get_blog(self):
        """method to test post a blog endpoint"""
        self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        response = self.app.get("/api/v1/questions/1")
        json.loads(response.data)
        self.assertEqual(response.status_code, 201)

    def test_get_nonexistingblog(self):
        """method to test post a blog endpoint"""
        self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        response = self.app.get("/api/v1/questions/51")
        json.loads(response.data)
        self.assertEqual(response.status_code, 201)


    
    def test_update_blog(self):
        """method to test post a blog endpoint"""
        self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        response = self.app.patch("/api/v1/questions/1/blog", headers={
                                  'Content-Type': 'application/json'}, data=json.dumps({"blog": "How to use Pytest"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 201)
    
    def test_update_nonextistingblog(self):
        """method to test post a blog endpoint"""
        self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        response = self.app.patch("/api/v1/questions/51/blog", headers={
                                  'Content-Type': 'application/json'}, data=json.dumps({"blog": "How to use Pytest"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_update_nonextistingtitle(self):
        """method to test post a blog endpoint"""
        self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        response = self.app.patch("/api/v1/questions/51/title", headers={
                                  'Content-Type': 'application/json'}, data=json.dumps({"title": "How to use Pytest"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 404)


    def test_update_title(self):
        """method to test update blog title endpoint"""
        self.app.post("/api/v1/questions",
                                 headers={'Content-Type': 'application/json'},data=json.dumps(self.blog))
        response = self.app.patch("/api/v1/questions/1/title", headers={
                                  'Content-Type': 'application/json'}, data=json.dumps({"title": "How to use Pytest"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 201)
    def test_delete_specific_blog(self):
        """method to test delete specific blog endpoint"""
        self.app.post("/api/v1/questions",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.blog))
        response = self.app.delete("/api/v1/questions/1")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('deleted', str(result))
        self.assertEqual(
        result['status'], 200)
    def test_delete_unavailable_blog(self):
        """method to test delete specific blog endpoint"""
        self.app.post("/api/v1/questions",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.blog))
        response = self.app.delete("/api/v1/questions/190")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('deleted', str(result))
        self.assertEqual(
        result['status'], 200)
        
        
     
        

    
