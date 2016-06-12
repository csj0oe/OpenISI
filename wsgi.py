<<<<<<< HEAD
#!/usr/bin/env python

from wsgiref.simple_server import make_server

from app.config import *

if __name__ == '__main__':
    from app.main import site_app as application
    httpd = make_server(host, port, application)
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
    httpd.serve_forever()
=======
#!/usr/bin/env python

#import os
#import sys
#sys.path.append(os.environ.get('OPENSHIFT_REPO_DIR','.'))
#virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')

from app.main import site_app as application

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8080, application)
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
    httpd.serve_forever()
>>>>>>> github/master
