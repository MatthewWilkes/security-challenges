from pyramid.response import Response

from pyramid.view import view_config


@view_config(route_name='one')
def one(request):
    name = request.GET.get('name')
    if name is None:
        return Response("Hello world")
    else:
        return Response("Hello %s" % name)

