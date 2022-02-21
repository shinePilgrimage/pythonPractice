from flask import *
from flask_restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
api = Api(app)


class infoView(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=inputs.regex(r'1[23456789]\d{9}'), help='手机号不正确')
        args = parser.parse_args()
        return args.phone


api.add_resource(infoView, '/phone/')
if __name__ == '__main__':
    app.run(debug=True)
