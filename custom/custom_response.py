import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


def get_body(receive_response):
    logging.info('\033[1;34mReceiving the request response\033[m')
    try:
        response_dictionary = receive_response.json()
    except Exception as errors:
        logging.error('\033[1;31mFailed to read body\033[m')
        raise Exception('failed to read body')
    else:
        logging.info('\033[1;34mSuccessfully read\033[m')
        return response_dictionary
