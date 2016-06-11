#!/usr/bin/env python

from sys import argv

from wsgiref.simple_server import make_server

from app.main import site_app as application

# Define server host
host = argv[1] if len(argv) > 1 else 'localhost'

# Define server port
port = argv[2] if len(argv) > 2 else 8080

# Define mongodb host
application.config['mongodb_host'] = argv[3] if len(argv) > 3 else 'localhost'

# Define mongodb port
application.config['mongodb_port'] = argv[4] if len(argv) > 4 else 27017

if __name__ == '__main__':
    httpd = make_server('127.6.68.129', 8080, application)
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
    httpd.serve_forever()