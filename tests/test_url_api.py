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
        response = client.post('url/encode', data=None, content_type='application/json')
        assert json.loads(response.get_data())['msg'] == "Bad Request"
        assert response.status_code == 400

        assert client.post('url/decode',
                           data=json.dumps({"s_url": ""}),
                           content_type='application/json').status_code == 400
        assert client.post('url/follow',
                           data=json.dumps({"s_url": ""}),
                           content_type='application/json').status_code == 400

    def test_api_invalid_url(self, client):
        response = client.post('url/encode',
                               data=json.dumps({"url": "not a url"}),
                               content_type='application/json')
        assert json.loads(response.get_data())['data'] == "Invalid URL"
        assert response.status_code == 400

        assert client.post('url/decode',
                           data=json.dumps({"s_url": "not a url"}),
                           content_type='application/json').status_code == 400
        assert client.post('url/follow',
                           data=json.dumps({"s_url": "not a url"}),
                           content_type='application/json').status_code == 400

    def test_decode_api_not_encoded(self, client):
        response = client.post('url/decode', data=json.dumps(encode_ok[1]), content_type='application/json')
        assert json.loads(response.get_data())['msg'] == "original url not found."

        response = client.post('url/follow', data=json.dumps(encode_ok[1]), content_type='application/json')
        assert json.loads(response.get_data())['msg'] == "original url not found."

    def test_encode_ok(self, client):
        response = client.post('url/encode', data=json.dumps(encode_ok[0]), content_type='application/json')

        assert response.status_code == 200
        assert json.loads(response.get_data())['s_url'] == encode_ok[1]['s_url']

    def test_decode_ok(self, client):
        client.post('url/encode', data=json.dumps(encode_ok[0]), content_type='application/json')
        response = client.post('url/decode', data=json.dumps(encode_ok[1]), content_type='application/json')

        assert response.status_code == 200
        assert json.loads(response.get_data())['url'] == encode_ok[0]['url']

    def test_follow_redirect(self, client):
        client.post('url/encode', data=json.dumps(encode_ok[0]), content_type='application/json')
        response = client.post('url/follow', data=json.dumps(encode_ok[1]), content_type='application/json')
        sleep(1)
        assert response.status_code == 302
        assert "redirected automatically to the target URL" in str(response.get_data())
