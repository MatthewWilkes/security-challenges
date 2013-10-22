from pyramid.view import view_config

from . import Layouts

class HomeView(Layouts):

    @view_config(route_name='home', renderer="templates/home.pt")
    def home(self):
        return {'challenges': {
            1:'one.py', 
            2:'two.py', 
            3:'three.py', 
        }}
    
