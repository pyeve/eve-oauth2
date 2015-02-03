# Eve-OAuth2

A [Eve-Demo][1] fork intended to demonstrate how you can protect API endpoints
by extending your [Eve][3] application with [Flask-OAuth2][3].

Flask-OAuth2 extends the main Eve application by providing a token creation
endpoint at `/oauth/token` and a users and clients management endpoint at
`/oauth/management`.

In order to be granted access to regular API endpoints (`/people/` and
`/works/`) a client must first obtain a valid token by hitting the token
creation endpoint with valid client id, username and password. The returned
token will then be used for subsequent requests until it eventually times out.
For details on how to perform token and endpoint requests see
[Flask-OAuth2][3].

## Distributed Services
Besides extending your Eve instance with Flask-OAuth2 you might also opt to
provide your auth service as a different, isolated application. This would be
a good choice if you are concerned about scalability and availability of your
services. Redis would then serve as a bridge between the applications, and
could itself reside on a different server, allowing for a totally distributed
and isolated network of (micro?) services.

## License
Eve-OAuth2 is a [Nicola Iarocci][5] and [Gestionali Amica][6] open source
project distributed under the [BSD license][7].

[1]: https://github.com/nicolaiarocci/eve-demo
[2]: http://python-eve.org
[3]: https://github.com/nicolaiarocci/flask-oauth2
[5]: http://nicolaiarocci.com
[6]: http://gestionaleamica.com
[7]: https://github.com/nicolaiarocci/eve-oauth2/blob/master/LICENSE
