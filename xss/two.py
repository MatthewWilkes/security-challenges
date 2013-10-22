import colander
from deform import Button
from deform import Form
from deform import ValidationFailure
from deform import widget
from pyramid.view import view_config, view_defaults

from . import Layouts

comments = []

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

@view_defaults(route_name='two', renderer="templates/two.pt")
class Two(Layouts):
        
    def __init__(self, context, request):
        super(Two, self).__init__(context, request)
        
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
        except ValidationFailure, e:
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
    
