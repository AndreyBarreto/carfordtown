
from flask import request
from functools import wraps
import jwt
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'HTTP_X_ACESS_TOKEN' in request.headers.environ:
            token = request.headers.environ['HTTP_X_ACESS_TOKEN']
        if not token:
            return {'error': 'Token is missing'}, 401

        try:
            jwt.decode(
                token, os.environ['SECRET_KEY'], algorithms=["HS256"])
        except:
            return {
                'error': 'Token is invalid'
            }, 401
        return f(*args, **kwargs)

    return decorated
