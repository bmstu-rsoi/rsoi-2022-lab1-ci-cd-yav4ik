from flask import Flask
from flask_restful import Api, Resource, reqparse


words = ["Hello", "world"]


class IDResource(Resource):
    print(1)

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(IDResource, "/id", "/id/", "/id/<int:id>")
    app.run(debug=True)

