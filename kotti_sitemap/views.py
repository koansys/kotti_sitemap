from kotti import DBSession
from kotti.resources import Content, Document
from pyramid.view import view_config


@view_config(name='sitemap.xml',
             context=Document,
             permission='view',
             renderer='templates/sitemap.pt',)
def sitemap(request):
    nodes = DBSession.query(Content).with_polymorphic(Content)
    request.response_content_type = "text/xml"
    return {'nodes': nodes}
