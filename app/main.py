from bottle import Bottle, run, static_file, template
from .web import web_app
from .ftp import ftp_app
from .mongodb import mongodb_app

site_app = Bottle()

site_app.merge(ftp_app)
site_app.merge(web_app)
site_app.merge(mongodb_app)

def start(h='localhost', p=80, d='.', db_h='localhost', db_p=3306):
	web_app.config['root_dir'] = d
	ftp_app.config['root_dir'] = d
	mongodb_app.config['mongodb_db_host'] = db_h
	mongodb_app.config['mongodb_db_port'] = db_p
	run(site_app, host=h, port=p, reloader=True)