from requests import get
import time

client_request = {
    'IP': '',
    'Header': [],
    'Body': '',
    'Method': '',
    'Url': '',
    'Date': '',
}


def new_client_request(ip, method, body, url):
    header = get(url).headers
    client_request['IP'] = ip
    client_request['Method'] = method
    client_request['Body'] = body
    client_request['Header'] = header
    return client_request

