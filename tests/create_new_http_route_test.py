from kittymocklib_py.mocker import Mocker


def test_create_http_route():
    mocker = Mocker("http://localhost", 6999)
    response, route = mocker.create_http_route(path="/create/location", method="POST", code=200, body="")
    assert response['status'] == 'success'