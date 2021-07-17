"""
It make request http.
"""
import logging
from http_client.send_request import send_request
from http_client.response import get_body


class HttpRoute:
    """
    It make request http.
    """
    def __init__(self, host, port, method, path):
        """
        Initialize the variables.
        :param host: string
        :param port: int
        :param method: string
        :param path: string
        """
        self.host = host
        self.port = port
        self.method = method
        self.path = path

    def get_history(self):
        """
        Get the historic of request made.
        :return: response dictionary
        """
        logging.info('\033[1;34mGetting all the histories\033[m')
        try:
            response = send_request(
                method='GET',
                url=f'{self.host}:{self.port}'
                    f'/=^.^=/history?path={self.path}'
                    f'&method={self.method}'
            )
            response_dictionary = get_body(response)
            logging.info('\033[1;34mSuccessfully obtained\033[m')
            return response_dictionary
        except Exception as error:
            logging.error('\033[1;31mFailed to get history,'
                          'Error: %(error)s\033[m')
            raise Exception(f'Failed to get history\n'
                            f'Error: {error}') from error

    def clear_history(self):
        """
        Clean the historic of request made.
        :return: response http
        """
        logging.info('\033[1;34mClearing the history\033[m')
        try:
            response = send_request(
                method='DELETE',
                url=f'{self.host}:{self.port}'
                    f'/=^.^=/history?path={self.path}'
                    f'&method={self.method}'
            )
            logging.info('\033[1;34mSuccessfully clean\033[m')
            return response
        except Exception as error:
            logging.error('\033[1;31mFailed to clear history,'
                          'Error: %(error)s\033[m')
            raise Exception(f'Failed to clear history\n'
                            f'Error: {error}') from error

    def delete(self):
        """
        Delete a route.
        :return: response http
        """
        logging.info('\033[1;34mDeleting the route\033[m')
        try:
            response = send_request(
                method='DELETE',
                url=f'{self.host}:{self.port}'
                    f'/=^.^=/route?path={self.path}'
                    f'&method={self.method}'
            )
            logging.info('\033[1;34mSuccessfully deleted\033[m')
            return response
        except Exception as error:
            logging.error('\033[1;31mFailed to delete http route,'
                          'Error: %(error)s\033[m')
            raise Exception(f'Failed to delete http route\n'
                            f'Error: {error}') from error

    def update(self, response_status, response_body):
        """
        Update the route.
        :param response_status: int
        :param response_body: string
        :return: response dictionary
        """
        logging.info('\033[1;34mUpdating the route\033[m')
        http_route = {
            "response": {
                "code": response_status,
                "body": response_body
            }
        }
        try:
            response = send_request(
                method='PUT',
                url=f'{self.host}:{self.port}'
                    f'/=^.^=/route?path={self.path}'
                    f'&method={self.method}',
                body=http_route
            )
            response_dictionary = get_body(response)
            logging.info('\033[1;34mSuccessfully updated\033[m')
            return response_dictionary
        except Exception as error:
            logging.error('\033[1;31mFailed to update route,'
                          'Error: %(error)s\033[m')
            raise Exception(f'Failed to update route\n'
                            f'Error: {error}') from error

    def details(self):
        """
        Get the details of route.
        :return: response dictionary
        """
        logging.info('\033[1;34mGetting the route\033[m')
        try:
            response = send_request(
                method='GET',
                url=f'{self.host}:{self.port}'
                    f'/=^.^=/route?path={self.path}'
                    f'&method={self.method}'
            )
            response_dictionary = get_body(response)
            logging.info('\033[1;34mSuccessfully obtained\033[m')
            return response_dictionary
        except Exception as error:
            logging.error('\033[1;31mFailed to get details http route,'
                          'Error: %(error)s\033[m')
            raise Exception(f'Failed to get details http route\n'
                            f'Error: {error}') from error

    def request(self, body='', hearders=''):
        """
        Make a request in route.
        :param body: string
        :param hearders: json
        :return: response http
        """
        logging.info('\033[1;34mReceiving a request '
                     'of method POST in route\033[m')
        try:
            response = send_request(
                method=self.method,
                url=f'{self.host}:{self.port}{self.path}',
                body=body,
                header=hearders
            )
            logging.info('\033[1;34mSuccessfully requested\033[m')
            return response
        except Exception as error:
            logging.error('\033[1;31mFailed to request http route,'
                          'Error: %(error)s\033[m')
            raise Exception(f'Failed to request http route\n'
                            f'Error: {error}') from error
