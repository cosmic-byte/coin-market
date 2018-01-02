from flask import request
from flask_restplus import Resource
from .util.dto import StudentDto
from ..service.userService import save_new_user, get_all_users


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
        return get_all_users()

    @api.response(201, 'Category successfully created.')
    @api.marshal_with(student)
    @api.doc('create a new student')
    @api.expect(student)
    def post(self):
        """Creates a new Student ."""
        data = request.json
        save_new_user(data=data)
        return None, 201
