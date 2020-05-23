from starlette.testclient import TestClient

from app import app

import ujson


def test_app():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert ujson.loads(response.content) == {"hello": "world"}
