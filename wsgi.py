#!/usr/bin/env python

from wsgiref.simple_server import make_server

from app.config import *

if __name__ == '__main__':
    from app.main import site_app as application
    httpd = make_server(host, port, application)
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
    httpd.serve_forever()
