from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

words = ["Hello", "world"]


class IDResource(Resource):
    def get(self):
        return words[0] + "" + words[1], 200


api.add_resource(IDResource, "/id", "/id/", "/id/<int:id>")


if __name__ == '__main__':
    app.run(debug=True)

