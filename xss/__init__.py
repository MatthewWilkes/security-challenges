from pyramid.renderers import get_renderer
from pyramid.decorator import reify
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_deform')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('deform_static', 'deform:static')

    config.add_route('home', '/')
    config.add_route('one', '/1')
    config.add_route('two', '/2')
    config.add_route('three', '/3')
    
    config.scan()
    return config.make_wsgi_app()


class Layouts(object):

    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @reify
    def global_template(self):
        renderer = get_renderer("templates/main_template.pt")
        return renderer.implementation().macros['layout']
