from json import decoder
from requests import get


j_send = {
    'Status': '',
    'Data': '',
    'Message': '',
}

def parse_jsend_data(http_response, data, url):
    http_response = get(url)
    if http_response != None:
        return http_response
    if http_response.status_code == 204:
        return None
    if data == None:
        data = {}
    jsend = j_send
    jsend['Data'] = data
    err = decoder(http_response, jsend)
    if err != None:
        return 'failed to parse jsend'
    if jsend['Status'] != 'sucess' or http_response.status_code >= 400:
        return f'{http_response.status_code}, {jsend["Message"]}'
    return None
