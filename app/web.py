import os

from bottle import Bottle, static_file

web_app = Bottle()
	
@web_app.route('/', method='GET')
@web_app.route('/web', method='GET')
@web_app.route('/web/', method='GET')
@web_app.route('/web/<filepath:path>', method='GET')
def site_web(filepath='index.html'):
	print('Filename: ' + os.path.basename(__file__))

    return static_file(filepath, root=web_app.config.get('root_dir')+'/web')