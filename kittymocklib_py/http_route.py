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