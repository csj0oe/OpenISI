import os

# current dir
repo_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../'))

# mongodb URL
mongodb_string = os.environ.get('OPENSHIFT_MONGODB_DB_URL','mongodb://admin:12345@localhost:27017/db')
