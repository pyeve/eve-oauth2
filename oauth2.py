# -*- coding: utf-8 -*-

"""
    A demostration of a simple BearerToken class.

    Active tokens are stored in redis via the Flask-Sentinel extension. When
    a request hits a API endpoint all we need to do is verify that a token
    is provided with the request and that said token is active.

    See https://github.com/nicolaiarocci/flask-sentinel

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
from eve.auth import BasicAuth
from flask import request
from redis import StrictRedis


class BearerAuth(BasicAuth):
    """ Overrides Eve's built-in basic authorization scheme and uses Redis to
    validate bearer token
    """
    def __init__(self):
        super(BearerAuth, self).__init__()
        self.redis = StrictRedis()

    def check_auth(self, token, allowed_roles, resource, method):
        """ Check if API request is authorized.

        Examines token in header and checks Redis cache to see if token is
        valid. If so, request is allowed.

        :param token: OAuth 2.0 access token submitted.
        :param allowed_roles: Allowed user roles.
        :param resource: Resource being requested.
        :param method: HTTP method being executed (POST, GET, etc.)
        """
        return token and self.redis.get(token)

    def authorized(self, allowed_roles, resource, method):
        """ Validates the the current request is allowed to pass through.

        :param allowed_roles: allowed roles for the current request, can be a
                              string or a list of roles.
        :param resource: resource being requested.
        """
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            token = None
        return self.check_auth(token, allowed_roles, resource, method)
