"""
test url api
"""
import json
import pytest

from time import sleep
from api import app
from tests.data import encode_ok


class TestUrlApi:
    @pytest.fixture
    def client(self):
        with app.test_client() as client:
            yield client

    def test_api_none_input(self, client):
        pass

    def test_api_invalid_url(self, client):
        pass

    def test_decode_api_not_encoded(self, client):
        pass

    def test_encode_ok(self, client):
        pass

    def test_decode_ok(self, client):
        pass

    def test_follow_redirect(self, client):
        pass
