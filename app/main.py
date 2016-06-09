from bottle import Bottle, run, static_file, template
from .web import web_app
from .ftp import ftp_app

site_app = Bottle()

site_app.merge(ftp_app)
site_app.merge(web_app)

def start(h='localhost', p=80, d='.'):
	web_app.config['root_dir'] = d
	ftp_app.config['root_dir'] = d
	run(site_app, host=h, port=p, reloader=True)