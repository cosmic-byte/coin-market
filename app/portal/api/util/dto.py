from flask_restplus import Namespace, fields

from app.portal.models.user import User


class UserDto:
    api = Namespace('user', description='user related operations')
    student = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    info = api.model('Personal_info', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class MessageDto:

    def __init__(self, message, created_on, user_id):
        self.message = message
        self.created_on = created_on
        self.user_id = user_id

    def get_username(self):
        user = User.query.filter_by(id=self.user_id).first()
        return user.username

    def serialize(self):
        return {
            'message': self.message,
            'created_on': str(self.created_on.time()),
            'username': self.get_username(),
        }