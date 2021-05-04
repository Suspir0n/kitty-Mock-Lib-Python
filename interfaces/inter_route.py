from inter_filter import IFilter
from inter_route_response import IRouteResponse


class IRoute:
    filters = IFilter()
    response = IRouteResponse()