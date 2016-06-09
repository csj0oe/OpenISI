import os
import inspect

from bottle import Bottle, static_file

ftp_app = Bottle()
	
@ftp_app.route('/ftp/<filepath:path>', method='GET')
def site_ftp(filepath):
	print('Filename: ' + os.path.basename(__file__))
	print('Action: ' + inspect.stack()[0][3])
	
    return static_file(filepath, root=ftp_app.config.get('root_dir')+'/ftp', 
    						download=True)
