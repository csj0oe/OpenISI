#!/usr/bin/env python

from sys import argv

from wsgiref.simple_server import make_server

from app.main import site_app as application

# Define server host
host = argv[1] if len(argv) > 1 else 'localhost'

# Define server port
port = int(argv[2]) if len(argv) > 2 else 8080

# Define mongodb host
mongodb_host = argv[3] if len(argv) > 3 else 'localhost'

# Define mongodb port
mongodb_port = argv[4] if len(argv) > 4 else '27017'

# Define mongodb user
mongodb_user = argv[5] if len(argv) > 5 else 'user'

# Define mongodb password
mongodb_pwd = argv[6] if len(argv) > 6 else 'password'

if __name__ == '__main__':
    httpd = make_server(host, port, application)
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
    httpd.serve_forever()