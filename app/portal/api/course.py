from flask_restplus import Resource
from .util.dto import CourseDto


api = CourseDto.api
course = CourseDto.course

course_mock = [
    {'title': "Control System", 'units': 3}
]


@api.route('/')
class CourseList(Resource):
    @api.doc('list_of_courses')
    @api.marshal_list_with(course)
    def get(self):
        """List all available courses"""
        return course_mock

