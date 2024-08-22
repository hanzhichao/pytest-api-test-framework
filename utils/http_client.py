import logging

import requests


class HttpClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url or ''
        self.session = requests.Session()

    def request(self, method: str, url: str, **kwargs) -> requests.Response:
        if not url.startswith('http'):
            url = f'{self.base_url.rstrip("/")}/{url.lstrip("/")}'

        logging.debug(f'Requesting {method} {url}')
        response = self.session.request(method, url, **kwargs)
        logging.debug(f'Response: {response.text}')
        return response

    def get(self, url: str, **kwargs) -> requests.Response:
        return self.request('GET', url, **kwargs)

    def post(self, url: str, **kwargs) -> requests.Response:
        return self.request('POST', url, **kwargs)

    def put(self, url: str, **kwargs) -> requests.Response:
        return self.request('PUT', url, **kwargs)

    def delete(self, url: str, **kwargs) -> requests.Response:
        return self.request('DELETE', url, **kwargs)
