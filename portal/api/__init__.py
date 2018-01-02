from flask_restplus import Api
from flask import Blueprint

from .auth import api as auth_ns
from .student import api as student_ns
from .course import api as course_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Student Management System',
          version='1.0',
          description='portal for university students '
          )

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(student_ns, path='/student')
api.add_namespace(course_ns, path='/course')
