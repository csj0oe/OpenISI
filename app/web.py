import os

from bottle import Bottle, static_file

from .config import repo_dir

web_app = Bottle()
	
@web_app.route('/', method='GET')
@web_app.route('/web', method='GET')
@web_app.route('/web/', method='GET')
@web_app.route('/web/<filepath:path>', method='GET')
def site_web(filepath='index.html'):
    return static_file('web/'+filepath, root=repo_dir+'/web')