from kittymocklib_py.mocker import Mocker
import unittest

class HappyWay(unittest.TestCase):
    def test_should_create_mock_server_using_valid_host(self):
        """
        Should Create a mock server using valid host and return a mocker server and a boolean with true value
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_create_http_mock_route_using_valid_data(self):
        """
        Create a new route in mock server and return route instance
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test1", "GET", 200, "test1 create http mock route")
        self.assertIsNotNone(route)
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_request_a_mocker_route_with_valid_method_and_path(self):
        """
        Request in a route with valid method and path
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test2", "GET", 200, "test2 request mock route")
        self.assertIsNotNone(route)
        route_response = route.request()
        self.assertEqual(route_response.status_code, 200)
        self.assertEqual(route_response.content, b"test2 request mock route")
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_delete_mocker_server(self):
        """
        Delete a mocker server and return true
        """
        mocker = Mocker("http://localhost", 6999)
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_delete_route_mock_server(self):
        """
        Delete a route in mock server and return true
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test3", "GET", 200, "test3 request mock route")
        self.assertIsNotNone(route)
        route_response = route.delete()
        self.assertEqual(route_response.status_code, 204)
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)
    
    def test_request_a_mocker_route_get_history_with_valid_port_and_filter(self):
        """
        Should get a history using a valid port and filter(path/method)
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test4", "GET", 200, "test4 request mock route")
        self.assertIsNotNone(route)
        route_response = route.get_history()
        self.assertEqual(route_response['status'], 'success')
        self.assertIsNotNone(route_response['data'])
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    def test_request_a_mocker_route_clean_history_in_route(self):
        """
        Clear history in a route
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test5", "GET", 200, "test5 request mock route")
        self.assertIsNotNone(route)
        route_response = route.clear_history()
        self.assertEqual(route_response.status_code, 204)
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)

    """def test_request_a_mocker_route_update(self):
        
        Should update a route passed the status response and body response
        
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test6", "GET", 200, "test6 request mock route")
        self.assertIsNotNone(route)
        route_response = route.update(204, "test6 update route")
        print(f'misera: {route_response}')
        self.assertEqual(route_response.status_code, 204)
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)"""

    def test_request_a_mocker_route_update(self):
        """
         Should get details of a route
        """
        mocker = Mocker("http://localhost", 6999)
        self.assertIsNotNone(mocker)
        route = mocker.create_http_route("/test7", "GET", 200, "test7 request mock route")
        self.assertIsNotNone(route)
        route_response = route.details()
        self.assertEqual(route_response['status'], 'success')
        self.assertEqual(route_response['data']['response']['body'], 'test7 request mock route')
        response = mocker.delete()
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()