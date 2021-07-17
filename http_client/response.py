"""
It receiving the request response and get body.
"""
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    datefmt='%d-%b-%y %H:%M:%S',
)
logger = logging.getLogger(__name__)


def get_body(receive_response):
    """
    It receiving the request response and get body.
    :param receive_response: json
    :return: response dictionary
    """
    logging.info('\033[1;34mReceiving the request response\033[m')
    try:
        response_dictionary = receive_response.json()
        logging.info('\033[1;34mSuccessfully read\033[m')
        return response_dictionary
    except Exception as error:
        logging.error('\033[1;31mFailed to read body, Error: %(error)s\033[m')
        raise Exception(f'failed to read body\n Error: {error}')