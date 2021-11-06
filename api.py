from flask import Flask, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)


class BookCoverService(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        ISBN = json_data["ISBN"]
        image = "https://covers.openlibrary.org/b/isbn/" + ISBN + "-M" + ".jpg"
        return_dict = {"Cover": image}
        return return_dict


api.add_resource(BookCoverService, '/book')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(port=port, debug=True)
