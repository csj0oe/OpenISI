<<<<<<< HEAD
from bottle import Bottle, run, static_file, template
from .web import web_app
from .ftp import ftp_app
from .mongodb import mongodb_app

site_app = Bottle()

site_app.merge(ftp_app)
site_app.merge(web_app)
site_app.merge(mongodb_app)
=======
from bottle import Bottle, run, static_file, template
from .web import web_app
from .ftp import ftp_app

site_app = Bottle()

site_app.merge(ftp_app)
site_app.merge(web_app)

if __name__ == '__main__':
    run(site_app, host=h, port=p, reloader=True)
>>>>>>> github/master
