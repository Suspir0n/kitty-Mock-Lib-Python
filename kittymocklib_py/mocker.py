"""
It create the mocker and a route http.
"""
import logging
from http_client.response import get_body
from http_client.send_request import send_request
from .http_route import HttpRoute

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    datefmt='%d-%b-%y %H:%M:%S'
)
logger = logging.getLogger(__name__)


class Mocker:
    """
    It create the mocker and a route http.
    """
    def __init__(self, host, port):
        """
        Initialize the variables and create mocker.
        :param host: string
        :param port: int
        """
        try:
            logging.info('\033[1;34mReceiving a request for create mocker\033[m')
            self.host = host
            self.port = port
            self.create_http_route_response = ''
            if host != 'http://localhost':
                return None
            response = send_request(
                method='POST',
                url=f'{host}:{port}/create'
            )
            response_dictionary = get_body(response)
            self.mocker_port = response_dictionary["data"]["port"]
            return None
        except Exception as error:
            logging.error('\033[1;31mFailed to create mocker, Error: %(error)s\033[m')
            raise Exception(f'Failed to create mocker\n Error: {error}') from error

    def create_http_route(self, path: str, method: str, code: int, body: str):
        """
        It create a http route.
        :param path: string
        :param method: string
        :param code: int
        :param body: string
        :return: functions of this route
        """
        try:
            logging.info('\033[1;34mReceiving a request for create http route\033[m')
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
            self.create_http_route_response = send_request(
                method='POST',
                url=f'{self.host}:{self.mocker_port}/=^.^=/route', body=http_route
            )
            logging.info('\033[1;34mSuccessfully created\033[m')
            return HttpRoute(
                host=self.host,
                port=self.mocker_port,
                method=method,
                path=path
            )
        except Exception as error:
            logging.error('\033[1;31mFailed to create http route, Error: %(error)s\033[m')
            raise Exception(f'Failed to create http route\n Error: {error}') from error

    def delete(self):
        """
        It delete the mocker.
        :return: response http
        """
        try:
            logging.info('\033[1;34mReceiving a request for delete mocker\033[m')
            response = send_request(method='DELETE', url=f'{self.host}:{self.mocker_port}')
            logging.info('\033[1;34mSuccessfully deleted\033[m')
            return response
        except Exception as error:
            logging.error('\033[1;31mFailed to delete mocker, Error: %(error)s\033[m')
            raise Exception(f'Failed to delete mocker\n Error: {error}') from error
