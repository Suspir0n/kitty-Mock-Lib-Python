import requests
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)

def send_request(method, url, body='', header=''):
    logging.info('\033[1;34mSending a request\033[m')
    try:
        if method == 'POST':
            logging.info('\033[1;34mRequesting a POST method request\033[m')
            request = requests.post(url, json=body, headers=header)
        if method == 'GET':
            logging.info('\033[1;34mRequesting a GET method request\033[m')
            request = requests.get(url)
        if method == 'PUT':
            logging.info('\033[1;34mRequesting a PUT method request\033[m')
            request = requests.put(url, json=body)
        if method == 'DELETE':
            logging.info('\033[1;34mRequesting a DELETE method request\033[m')
            request = requests.delete(url)
        logging.info('\033[1;34mSuccessfully requesting\033[m')
        return request
    except Exception as error:
        logging.error(f'\033[1;31mError requesting a request, Error: {error}\033[m')
        raise Exception(f'Error during request request!\n Error: {error}')