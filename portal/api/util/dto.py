from flask_restplus import Namespace, fields


class CourseDto:
    api = Namespace('course', description='course related operations')
    course = api.model('course', {
        'title': fields.String(required=True, description='The title of the course'),
        'units': fields.Integer(required=True, description='The unit of the course '),
    })


class StudentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        'email': fields.String(required=True, description='students email address'),
        'first_name': fields.String(required=True, description='students first_name'),
        'last_name': fields.String(required=True, description='students last_name'),
        'username': fields.String(required=True, description='students username'),
        'public_id': fields.String(required=True, description='students public Identity'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    info = api.model('Personal_info', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
