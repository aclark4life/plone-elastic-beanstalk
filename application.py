# def application(environ, start_fn):
#     start_fn('200 OK', [('Content-Type', 'text/html')])
#     return ["<h1>Hello world!</h1>\n"]

from Zope2.Startup.run import make_wsgi_app

application = make_wsgi_app({}, '/srv/parts/plone/etc/zope.conf')
