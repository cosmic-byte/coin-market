from flask_restplus import Api
from flask import Blueprint

from .auth import api as auth_ns
from .user import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Crypto Currency Market Platform',
          version='1.0',
          description='a platform for people to make crypto transactions'
          )

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(user_ns, path='/user')
