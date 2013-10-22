from pyramid.response import Response
from . import Layouts

from pyramid.view import view_config, view_defaults

@view_defaults(route_name='two')
class Two(Layouts):
        
    @view_config(request_method="GET")
    def get(self):
        name = self.request.GET.get('name')
        if name is None:
            return Response("Hello world")
        else:
            return Response("Hello %s" % name)

