from flask import Flask, request, Response
from base64 import b64decode
import secrets

app = Flask(__name__)

CLIENT_ID = "my_client_id"
CLIENT_SECRET = "my_client_secret"


@app.route('/token', methods=['POST'])
def token():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return Response('Missing authorization header', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    try:
        scheme, credentials = auth_header.split(' ')
        if scheme.lower() == 'basic':
            decoded_credentials = b64decode(credentials).decode('utf-8')
            client_id, client_secret = decoded_credentials.split(':')

            if secrets.compare_digest(client_id, CLIENT_ID) and secrets.compare_digest(client_secret, CLIENT_SECRET):
                # Normally, you would return an access token here.
                # We're just returning a success message for simplicity.
                return "Authentication successful", 200

    except (ValueError, TypeError):
        pass

    return Response('Could not authenticate. Invalid client id or client secret', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
