from custom.custom_send_request import send_request
from custom.custom_response import get_body
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
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
        except Exception as errors:
            logging.error('\033[1;31mFailed to get history\033[m')
            raise Exception('Failed to get history')
        else:
            logging.info('\033[1;34mSuccessfully obtained\033[m')
            return response_dictionary

    def clear_history(self):
        logging.info('\033[1;34mClearing the history\033[m')
        try:
            response = send_request(method='DELETE', url=f'{self.host}:{self.port}/=^.^=/history?path={self.path}&method={self.method}')
            response_dictionary = get_body(response)
        except Exception as errors:
            logging.error('\033[1;31mFailed to clear history\033[m')
            raise Exception('Failed to clear history')
        else:
            logging.info('\033[1;34mSuccessfully clean\033[m')
            return response_dictionary

    def delete(self):
        logging.info('\033[1;34mDeleting the route\033[m')
        try:
            response = send_request(method='DELETE', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}')
            response_dictionary = get_body(response)
        except Exception as errors:
            logging.error('\033[1;31mFailed to delete http route\033[m')
            raise Exception('Failed to delete http route')
        else:
            logging.info('\033[1;34mSuccessfully deleted\033[m')
            return response_dictionary

    def update(self, response_status, response_body):
        logging.info('\033[1;34mUpdating the route\033[m')
        http_route = {
            "response": {
                "code": response_status,
                "body": response_body
            }
        }
        try:
            response = send_request(method='UPDATE', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}', body=http_route)
            response_dictionary = get_body(response)
        except Exception as errors:
            logging.error('\033[1;31mFailed to update route\033[m')
            raise Exception('Failed to update route')
        else:
            logging.info('\033[1;34mSuccessfully updated\033[m')
            return response_dictionary

    def details(self):
        logging.info('\033[1;34mGetting the route\033[m')
        try:
            response = send_request(method='GET', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}')
            response_dictionary = get_body(response)
        except Exception as errors:
            logging.error('\033[1;31mFailed to get details http route\033[m')
            raise Exception('Failed to get details http route')
        else:
            logging.info('\033[1;34mSuccessfully obtained\033[m')
            return response_dictionary

    """def send(self):
        response = send_request(method='POST', url=f'{self.host}:{self.port}/=^.^=/route?path={self.path}&method={self.method}')
        response_dictionary = get_body(response)
        return response_dictionary"""