
def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_sitemap'


def includeme(config):
    config.scan(__name__)
