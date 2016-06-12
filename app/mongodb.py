import os
import json

from bottle import Bottle, request, abort
from pymongo import MongoClient

from .config import *

mongodb_app = Bottle()
 
con_str = 'mongodb://'+mongodb_user+':'+mongodb_pwd+'@'+mongodb_host+':'+mongodb_port
client = MongoClient(con_str)
db = client.diy

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

@mongodb_app.route('/documents/<id>', method='GET')
def get_document(id):
    entity = db.docs.find_one({'_id':id})
    if not entity:
        abort(404, 'No document found')
    return entity