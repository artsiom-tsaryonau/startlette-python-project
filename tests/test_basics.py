from starlette.testclient import TestClient

from app import app

import ujson


def test_app():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert ujson.loads(response.content) == {'hello': 'world'}


def test_path_parameter_app():
    client = TestClient(app)
    response = client.get('/path/User')
    assert response.status_code == 200
    assert ujson.loads(response.content) == {'hello': 'User'}


def test_headers_app():
    client = TestClient(app)
    response = client.get('/headers',
                          headers={'content-type': 'application/xml'})
    assert response.status_code == 200
    assert ujson.loads(response.content) == {'content-type': 'application/xml'}


def test_get_parameters_app():
    client = TestClient(app)
    response = client.get('/params?query=abc')
    assert response.status_code == 200
    assert ujson.loads(response.content) == {'query': 'abc'}
