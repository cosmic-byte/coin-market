from flask_restplus import Namespace, Resource, fields

api = Namespace('auth', description='authentication related operations')

info = api.model('Personal_info', {
    'email': fields.String(required=True, description='The email address'),
    'password': fields.String(required=True, description='The user password '),
})

Users = [
    {'email': 'greg@gmail.com', 'password': 'blake007'},
]


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(info)
    def get(self):
        """List all cats"""
        return Users


@api.route('/<email>')
@api.param('email', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(info)
    def get(self, email):
        """Fetch a user given its identifier"""
        for user in Users:
            if user['email'] == email:
                return user
        api.abort(404)
