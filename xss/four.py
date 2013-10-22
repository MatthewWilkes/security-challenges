import re

import colander
from deform import Button
from deform import Form
from deform import ValidationFailure
from deform import widget
from pyramid.view import view_config, view_defaults

from . import Layouts

comments = []

TAGS = re.compile("<([a-z]+)")

HANDLERS = re.compile("<.*?(on[a-z]+).*?>")

SAFE_TAGS = set(('p', 'img', 'div', 'br', 'span', 'h1', 'h2', 'h3', 'em', 'b', 
                 'strong', 'i', 'ol', 'ul', 'li', 'blockquote', 'pre', 'sup', 
                 'sub', 'code'))

def safe_html(node, value):
    tags_used = set(TAGS.findall(value))
    if not tags_used < SAFE_TAGS:
        raise colander.Invalid(node, 'You have entered HTML tags that are not allowed')
    if HANDLERS.findall(value)
        raise colander.Invalid(node, 'Javascript handlers are not allowed')

class GuestBookSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(),
            title="Name",
            required=True,
            )

    comment = colander.SchemaNode(colander.String(),
            widget=widget.RichTextWidget(),
            title="Comment",
            required=True,
            validator=safe_html,
            )

@view_defaults(route_name='four', renderer="templates/two.pt")
class Four(Layouts):
        
    def __init__(self, context, request):
        super(Four, self).__init__(context, request)
        
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
        try:
            appstruct = self.form.validate(controls)
        except ValidationFailure as e:
            return {
                'form': e.render(),
                'js': self.form.get_widget_resources()['js'],
                'css': self.form.get_widget_resources()['css'],
                'comments': comments,
            }
        
        # So, obviously, in real life this would go in a database,
        # but I CBA, so I'm using a global value as my DB
        comments.append(appstruct)
        return {'form':'', 'comments':comments}
    
