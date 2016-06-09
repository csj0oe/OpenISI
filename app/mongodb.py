import json
from bottle import Bottle, request, abort
from pymongo import Connection

mongodb_app = Bottle()
 
connection = Connection(mongodb_app.config.get('mongodb_db_host'),
                        mongodb_app.config.get('mongodb_db_port'))
db = connection.mydatabase
 
@mongodb_app.route('/documents', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
     
@mongodb_app.route('/documents/:id', method='GET')
def get_document(id):
    entity = db['documents'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity