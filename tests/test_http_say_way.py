"""
Testing the say way of kittymocklib-py
"""
import unittest
from kittymocklib_py.mocker import Mocker


class SayWay(unittest.TestCase):
    """
    Testing the say way of kittymocklib-py
    """
    def test_should_create_mock_server_using_invalid_host(self):
        """
        Create a mocker with a inexistence host
        """
        mocker = Mocker("INVALID", 6999)
        self.assertIsNotNone(mocker)

    def test_should_create_http_mock_route_using_invalid_path(self):
        """
        Create a route with a invalid path
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route(
            "INVALID",
            "GET",
            200,
            "test1 create http mock route"
        )
        self.assertIsNotNone(route)
        self.assertEqual(mocker.create_http_route_response.status_code, 400)
        self.assertEqual(
            mocker.create_http_route_response.json()['message'],
            'request with invalid route path'
        )
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_should_create_http_mock_route_using_invalid_method(self):
        """
        Create a route with a invalid method
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route(
            "/test2",
            "INVALID",
            200,
            "test2 create http mock route"
        )
        self.assertIsNotNone(route)
        self.assertEqual(mocker.create_http_route_response.status_code, 400)
        self.assertEqual(
            mocker.create_http_route_response.json()['message'],
            'request with invalid route method'
        )
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_should_create_http_mock_route_using_invalid_response_code(self):
        """
        Create a route with a invalid response code
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route(
            "/test2",
            "GET",
            9999,
            "test2 create http mock route"
        )
        self.assertIsNotNone(route)
        self.assertEqual(mocker.create_http_route_response.status_code, 400)
        self.assertEqual(
            mocker.create_http_route_response.json()['message'],
            'request with invalid route response code'
        )
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
