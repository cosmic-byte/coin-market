from functools import wraps

import jwt
from flask import request

from app.portal.config import key


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-AUTH-KEY' in request.headers:
            token = request.headers['X-AUTH-KEY']

        if not token:
            return {'message': 'Token is missing.'}, 401

        try:
            data = jwt.decode(token, key)

        except:
            return {'message': 'Token is invalid.'}, 401

        return f(*args, **kwargs)

    return decorated
