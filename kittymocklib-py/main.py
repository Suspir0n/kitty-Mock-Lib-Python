import requests

class HTTP_Route:
    def __init__(self, host, port, method, path):
        self.host = host
        self.port = port
        self.method = method
        self.path = path

    def get_history(self):
        response = requests.get(f'{self.host}:{self.port}/=^.^=/history?path={self.path}&method={self.method}')
        response_dictionary = response.json() 
        return response_dictionary['data'] 


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
        response = requests.post(f'{self.host}:{self.mocker_port}/=%5E.%5E=/route', json=http_route)
        print(response.json())
        return HTTP_Route(host=self.host, port=self.mocker_port, method=method, path=path)


def __init__():
    mocker = Mocker("http://localhost", 6999)
    route = mocker.create_http_route(path="/create/location", method="POST", code=200, body="")
    requests.post(f'http://localhost:{mocker.mocker_port}/create/location', json={'Hello': 'olá'})
    print(route.get_history())
    print(mocker.mocker_port)



__init__()