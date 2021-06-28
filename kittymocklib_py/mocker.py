from .http_route import HTTP_Route
from custom.custom_send_request import send_request
from custom.custom_response import get_body

class Mocker:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        response = send_request(method='POST', url=f'{host}:{port}/create')
        response_dictionary = get_body(response)
        self.mocker_port = response_dictionary["data"]["port"]

    def create_http_route(self, path: str, method: str, code: int, body: str):
        http_route = {
            "filters": {
                "path": path,
                "method": method
            },
            "response": {
                "code": code,
                "body": body
            }
        }
        response = send_request(method='POST', url=f'{self.host}:{self.mocker_port}/=^.^=/route', body=http_route)
        response_dictionary = get_body(response)
        return response_dictionary, HTTP_Route(host=self.host, port=self.mocker_port, method=method, path=path)