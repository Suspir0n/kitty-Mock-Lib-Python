from json import encoder
from requests import request as req


def send_json_request(method, url, data):
    body = encoder(data)
    if body != None:
        return None, 'failed to encode request'
    return send_request(method, url, body, None)


def send_request(method, url, body, header):
    request = req(method, url, body)
    if request != None:
        return None, 'failed to create request'
    request.headers = header