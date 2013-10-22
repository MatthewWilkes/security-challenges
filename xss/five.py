import re

import colander
from deform import Button
from deform import Form
from deform import ValidationFailure
from deform import widget
from lxml.html.clean import Cleaner
from pyramid.view import view_config, view_defaults

from . import Layouts

comments = []

TAGS = re.compile("<([a-z]+)")

SAFE_TAGS = set(('p', 'img', 'div', 'br', 'span', 'h1', 'h2', 'h3', 'em', 'b', 
                 'strong', 'i', 'ol', 'ul', 'li', 'blockquote', 'pre', 'sup', 
                 'sub', 'code'))

class GuestBookSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(),
            title="Name",
            required=True,
            )

    comment = colander.SchemaNode(colander.String(),
            widget=widget.RichTextWidget(),
            title="Comment",
            required=True,
            )

@view_defaults(route_name='five', renderer="templates/two.pt")
class Five(Layouts):
        
    def __init__(self, context, request):
        super(Five, self).__init__(context, request)
        
        schema = GuestBookSchema().bind()
        button = Button(name="submit", title="Submit")
        self.form = Form(schema, buttons=(button,))
    
    @view_config(request_method="GET")
    def get(self):
        return {
            'form': self.form.render(),
            'js': self.form.get_widget_resources()['js'],
            'css': self.form.get_widget_resources()['css'],
            'comments': comments,
        }

    @view_config(request_method="POST", request_param="submit")
    def post(self):
        controls = self.request.POST.items()
        
        cleaner = Cleaner(scripts=True, javascript=True, links=True, 
                meta=True, embedded=True, safe_attrs_only=True)
        
        try:
            appstruct = self.form.validate(controls)
        except ValidationFailure as e:
            return {
                'form': e.render(),
                'js': self.form.get_widget_resources()['js'],
                'css': self.form.get_widget_resources()['css'],
                'comments': comments,
            }
        
        # Filter bad HTML
        appstruct['comment'] = cleaner.clean_html(appstruct['comment'])
        
        # So, obviously, in real life this would go in a database,
        # but I CBA, so I'm using a global value as my DB
        comments.append(appstruct)
        return {'form':'', 'comments':comments}
    
