from kotti import DBSession
from kotti.resources import Content
from kotti.resources import Document


def sitemap(request):
    nodes = DBSession.query(Content).with_polymorphic(Content)
    request.response_content_type = "text/xml"
    return {'nodes': nodes}


def includeme(config):
    config.add_view(
        sitemap,
        context=Document,
        name='sitemap.xml',
        permission='view',
        renderer='templates/sitemap.pt',
        )
