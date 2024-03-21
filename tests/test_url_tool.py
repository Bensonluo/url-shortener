"""
test_url_tool methods
"""
import pytest

from tests.data import urls
from api.tools import url_tool


class TestUrlTool:
    @pytest.fixture(params=urls)
    def url(self, request):
        return request.param

    def test_url_encode(self, url):
        encoded = url_tool.encode_url(url[0])
        assert encoded == url[1]

    def test_url_decode(self, url):
        decoded = url_tool.decode_url(url[1])
        assert decoded == url[0]
