"""Tornado App Start."""

import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
from django.core.wsgi import get_wsgi_application


def main():
    """Main entry when running this module."""
    os.environ['DJANGO_SETTINGS_MODULE'] = 'eambulance.settings'
    application = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
