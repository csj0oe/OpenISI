from bottle import Bottle, run, static_file, template
from .config import repo_dir

ftp_app = Bottle()
	
@ftp_app.route('/ftp/<filepath:path>', method='GET')
def site_ftp(filepath):
    return static_file(filepath, root=repo_dir+'/ftp', download=True)
