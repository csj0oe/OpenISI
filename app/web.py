from bottle import Bottle, static_file, request, abort
from pymongo import MongoClient

import json

client = MongoClient('mongodb://admin:veAcrpgiBLl5@127.6.68.130:27017')
db = client.diy

web_app = Bottle()
	
@web_app.route('/', method='GET')
@web_app.route('/<filepath:path>', method='GET')
@web_app.route('/web', method='GET')
@web_app.route('/web/', method='GET')
@web_app.route('/web/<filepath:path>', method='GET')
def site_web(filepath='index.html'):
    return static_file(filepath, root=web_app.config.get('root_dir')+'/web')


@web_app.route('/documents', method='POST')
def post_document():
    entity = request.json
    if not entity:
        abort(400, 'No data received')
    if '_id' not in entity:
        abort(400, 'No _id specified')
    try:
        db.docs.insert_one(entity)
    except Exception as ve:
        abort(400, str(ve))


@web_app.route('/documents/<id>', method='GET')
def get_document(id):
    entity = db.docs.find_one({'_id':id})
    if not entity:
        abort(404, 'No document found')
    return entity