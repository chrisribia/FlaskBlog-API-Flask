from flask import jsonify,make_response,request
from flask_restful import Resource

chris = [1,2,5,6,8,7]
class hello(Resource):

    def __init__(self):
        self.db = chris
    

    def get(self):
        return jsonify({"status" : 200,
                        "message" : self.db[0]})