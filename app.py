# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
import socket
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    
    def get(self):
       	return {'hello':'world', 'fqdn':socket.getfqdn()}
api.add_resource(HelloWorld, '/')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
