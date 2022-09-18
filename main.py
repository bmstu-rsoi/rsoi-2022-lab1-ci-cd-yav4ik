from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)

words = ["Hello", "world"]


class IDResource(Resource):
    def get(self):
        return words[0] + "" + words[1], 200


if __name__ == '__main__':
    api = Api(app)
    api.add_resource(IDResource, "/id", "/id/", "/id/<int:id>")
    app.run(debug=True)

