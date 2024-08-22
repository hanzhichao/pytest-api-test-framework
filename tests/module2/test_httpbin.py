import logging

import pytest


class TestHttpbinGet(object):
    def test_httpbin_get(self, http):
        resp = http.get('/get', params={'a': 1, 'b': 2})
        print(resp.text)
