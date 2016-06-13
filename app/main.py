from bottle import Bottle, run
from .web import web_app
from .ftp import ftp_app
from .mongodb import mongodb_app

site_app = Bottle()

site_app.merge(mongodb_app)
site_app.merge(ftp_app)
site_app.merge(web_app)

if __name__ == '__main__':
    run(site_app, host=h, port=p, reloader=True)
