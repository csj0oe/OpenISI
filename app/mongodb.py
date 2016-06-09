import json
from bottle import Bottle, request, abort
from pymongo import MongoClient

mongodb_app = Bottle()
 
client = MongoClient('mongodb://admin:veAcrpgiBLl5@127.6.68.130:27017')
db = client.diy

@mongodb_app.route('/a/<filepath:path>', method='GET')
def site_ftp(filepath):
    return filepath

@mongodb_app.route('/documents/<docid>', method='GET')
def get_document(docid):
    entity = db.docs.find_one({'_id':docid})
    print(type(entity))
    print(entity)
    if not entity:
        abort(404, 'No document found')
    return entity

@mongodb_app.route('/documents', method='POST')
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