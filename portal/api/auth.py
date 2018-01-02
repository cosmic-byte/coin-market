from flask_restplus import Resource
from .util.dto import AuthDto


api = AuthDto.api
info = AuthDto.info

Users = [
    {'email': 'greg@gmail.com', 'password': 'blake007'},
]


@api.route('/login')
class UserLogin(Resource):
    @api.doc('student login')
    @api.marshal_with(info)
    def get(self):
        """Login user"""
        return Users

