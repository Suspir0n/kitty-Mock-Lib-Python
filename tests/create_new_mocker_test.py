from kittymocklib_py.mocker import Mocker


def test_create_mocker():
    created_mocker = Mocker("http://localhost", 6999)
    assert created_mocker.mocker_port
