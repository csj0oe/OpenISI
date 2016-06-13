from bottle import Bottle, request, abort
from pymongo import MongoClient
from .config import mongodb_string

mongodb_app = Bottle()
 
client = MongoClient(mongodb_string)
#db = client.get_default_database() - Needs PyMongo > 2.6 , Currently we use 2.5
# begin solution
db = client['openisi']
# end solution

@mongodb_app.route('/documents', method='POST')
def post_document():
    entity = request.json
    if not entity:
        abort(400, 'No data received')
    if '_id' not in entity:
        abort(400, 'No _id specified')
    try:
        db.docs.insert(entity)
    except Exception as ve:
        abort(400, str(ve))

@mongodb_app.route('/documents/<id>', method='GET')
def get_document(id):
    entity = db.docs.find_one({'_id':id})
    if not entity:
        abort(404, 'No document found')
    return entity