from flask_restplus import Resource
from .util.dto import StudentDto


api = StudentDto.api
student = StudentDto.student

student_mock = [
    {'email': 'greg@gmail.com', 'username': 'blake007', 'first_name': 'Greg', 'last_name': 'Greg', 'public_id': '1002'},
]


@api.route('/')
class StudentList(Resource):
    @api.doc('list_of_students')
    @api.marshal_list_with(student)
    def get(self):
        """List all available students"""
        return student_mock

