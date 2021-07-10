from http_client.send_request import send_request
from http_client.response import get_body
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)

class HTTP_Route:
    def __init__(self, host, port, method, path):
        self.host = host
        self.port = port
        self.method = method
        self.path = path

    def get_history(self):
        logging.info('\033[1;34mGetting all the histories\033[m')
        try:
            response = send_request(method='GET', url=f'{self.host}:{self.port}/=^.^=/history?path={self.path}&method={self.method}')
            response_dictionary = get_body(response)
            logging.info('\033[1;34mSuccessfully obtained\033[m')
            return response_dictionary
        except Exception as error:
            logging.error(f'\033[1;31mFailed to get history, Error: {error}\033[m')
            raise Exception(f'Failed to get history\n Error: {error}')

    def clear_history(self):
        logging.info('\033[1;34mClearing the history\033[m')
        try:
            response = send_request(method='DELETE', url=f'{self.host}:{self.port}/=^.^=/history?path={self.path}&method={self.method}')
            logging.info('\033[1;34mSuccessfully clean\033[m')
            return response
        except Exception as error:
            logging.error(f'\033[1;31mFailed to clear history, Error: {error}\033[m')
            raise Exception(f'Failed to clear history\n Error: {error}')

    def delete(self):
        logging.info('\033[1;34mDeleting the route\033[m')
        try:
            response = send_request(method='DELETE', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}')
            logging.info('\033[1;34mSuccessfully deleted\033[m')
            return response
        except Exception as error:
            logging.error(f'\033[1;31mFailed to delete http route, Error: {error}\033[m')
            raise Exception(f'Failed to delete http route\n Error: {error}')

    def update(self, response_status, response_body):
        logging.info('\033[1;34mUpdating the route\033[m')
        http_route = {
            "response": {
                "code": response_status,
                "body": response_body
            }
        }
        try:
            response = send_request(method='PUT', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}', body=http_route)
            response_dictionary = get_body(response)
            logging.info('\033[1;34mSuccessfully updated\033[m')
            return response_dictionary
        except Exception as error:
            logging.error(f'\033[1;31mFailed to update route, Error: {error}\033[m')
            raise Exception(f'Failed to update route\n Error: {error}')

    def details(self):
        logging.info('\033[1;34mGetting the route\033[m')
        try:
            response = send_request(method='GET', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}')
            response_dictionary = get_body(response)
            logging.info('\033[1;34mSuccessfully obtained\033[m')
            return response_dictionary
        except Exception as error:
            logging.error(f'\033[1;31mFailed to get details http route, Error: {error}\033[m')
            raise Exception(f'Failed to get details http route\n Error: {error}')

    def request(self, body='', hearders=''):
        logging.info('\033[1;34mReceiving a request of method POST in route\033[m')
        try:
            response = send_request(method=self.method, url=f'{self.host}:{self.port}{self.path}', body=body, header=hearders)
            logging.info('\033[1;34mSuccessfully requested\033[m')
            return response
        except Exception as error:
            logging.error(f'\033[1;31mFailed to request http route, Error: {error}\033[m')
            raise Exception(f'Failed to request http route\n Error: {error}')