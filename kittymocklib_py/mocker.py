import requests
from .http_route import HTTP_Route

class Mocker:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        response = requests.post(f'{host}:{port}/create')
        response_dictionary = response.json()
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
        response = requests.post(f'{self.host}:{self.mocker_port}/=^.^=/route', json=http_route)
        response_dictionary = response.json()
        return response_dictionary, HTTP_Route(host=self.host, port=self.mocker_port, method=method, path=path)