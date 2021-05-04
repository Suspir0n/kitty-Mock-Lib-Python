from inter_route import IRoute
from inter_response import IResponse
from inter_filter import IFilter


class IMockerHttp:

    def create_route(self, route=IRoute):
        pass


    def request_route(self, path):
        pass


    def delete_route(self):
        pass


    def get_route_history(self):
        pass


    def clear_route_history(self):
        pass


    def delete_mocker(self):
        pass