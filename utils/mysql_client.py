import pymysql
import re

from urllib.parse import urlparse
from urllib.parse import parse_qs

DEFAULT_MYSQL_PORT = 3306
DEFAULT_MYSQL_CHARSET = 'utf8'


def parse_db_uri(db_uri: str):
    # db = mysql://root:passw0rd@127.0.0.1:3360/testdb
    pass


class MySQLClient:
    def __init__(self, db_uri: str):
        parsed_uri = urlparse(db_uri)
        assert parsed_uri.scheme == 'mysql'

        user = parsed_uri.username
        password = parsed_uri.password
        host = parsed_uri.hostname
        port = parsed_uri.port or DEFAULT_MYSQL_PORT
        db = parsed_uri.fragment

        assert db != ''

        charset = DEFAULT_MYSQL_CHARSET
        if parsed_uri.query is not None:
            charset = parse_qs(parsed_uri.query).get('charset', [DEFAULT_MYSQL_CHARSET])[0]

        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset,
                                    autocommit=True)
        self.cursor = self.conn.cursor()

    def execute(self, sql: str, params=None):
        pass

    def query_one(self, sql: str, params=None):
        pass

    def query_all(self, sql: str, params=None):
        pass


if __name__ == '__main__':
    r = urlparse('smtp://test_results@sina.com:6face3c049176c12@smtp.sina.com')
    print(r.query)
    print(r.scheme)
    print('db: ', repr(r.fragment))
    print('user', r.username)
    print('host', r.hostname)
    print(r.port)
    # 'alex'

    print(r.password)
    print(parse_qs(r.query).get('charset'))
