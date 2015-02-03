# -*- coding: utf-8 -*-

"""
    Eve Demo (Secured)
    ~~~~~~~~~~~~~~~~~~

    This is a fork of Eve Demo (https://github.com/nicolaiarocci/eve-demo)
    intended to demonstrate how a Eve API can be secured by means of
    Flask-Sentinel.

    For demonstration purposes, besides protecting a couple API endpoints
    with a BearerToken class instance, we are also adding a static html
    endpoint an protecting with via decorator.

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

from eve import Eve
from oauth2 import BearerAuth
from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth

app = Eve(auth=BearerAuth)
ResourceOwnerPasswordCredentials(app)


@app.route('/endpoint')
@oauth.require_oauth()
def restricted_access():
    return "You made it through and accessed the protected resource!"

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
