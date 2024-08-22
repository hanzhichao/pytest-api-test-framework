from emailz import email
from urllib.parse import urlparse, parse_qs

DEFAULT_SMTP_SSL = True
DEFAULT_SMTP_PORT = None


class EmailClient:
    def __iter__(self, stmp_uri: str):
        parsed_uri = urlparse(stmp_uri)
        assert parsed_uri.scheme == 'stmp'

        user = parsed_uri.username
        password = parsed_uri.password
        host = parsed_uri.hostname
        port = parsed_uri.port or DEFAULT_SMTP_SSL
        ssl = DEFAULT_SMTP_SSL
        if parsed_uri.query is not None:
            sslmode = parse_qs(parsed_uri.query).get('sslmode', [''])[0]
            if sslmode == 'disable':
                ssl = False

        email.config(host=host, port=port, user=user, password=password, ssl=ssl)

    def send(self, stmp_uri: str):
        pass