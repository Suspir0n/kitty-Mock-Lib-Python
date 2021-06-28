import requests
from kittymocklib_py.mocker import Mocker


def test_get_history():
    mocker = Mocker("http://localhost", 6999)
    response, route = mocker.create_http_route(path="/create/location", method="POST", code=200, body="")
    requests.post(f'http://localhost:{mocker.mocker_port}/create/location', json={'Hello': 'olá'})
    assert route.get_history()