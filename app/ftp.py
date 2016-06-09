from bottle import Bottle, run, static_file, template

ftp_app = Bottle()
	
@ftp_app.route('/ftp/<filepath:path>', method='GET')
def site_ftp(filepath):
    return static_file(filepath, root=ftp_app.config.get('root_dir')+'/ftp', 
    						download=True)
