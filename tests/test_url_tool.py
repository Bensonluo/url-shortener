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
        pass

    def test_url_decode(self, url):
        pass
