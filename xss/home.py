from pyramid.view import view_config

from . import Layouts

class HomeView(Layouts):

    @view_config(route_name='home', renderer="templates/home.pt")
    def home(self):
        return {'challenges': (1,2, )}
    
