


route = {
    'host': '',
    'method': '',
    'path': '',
    'response_body': '',
    'response_status': '',
    'mocker': '',
}


def new_http_route(host, method, path, response_body, response_status, mocker):
    route['host'] = host
    route['method'] = method
    route['path'] = path
    route['response_body'] = response_body
    route['response_status'] = response_status
    route['mocker'] = mocker
    return route