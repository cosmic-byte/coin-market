from flask_restplus import Api
from flask import Blueprint

from .view import api as ns1

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Authentication',
          version='1.0',
          description='authentication related '
          )

api.add_namespace(ns1, path='/auth')
