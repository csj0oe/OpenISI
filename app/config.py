import os
from sys import argv
import configparser

# Define repo dir
repo_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../'))

# Vars from command line argv
host = argv[1] if len(argv) > 1 else 'localhost'
port = int(argv[2]) if len(argv) > 2 else 8080
mongodb_host = argv[3] if len(argv) > 3 else 'localhost'
mongodb_port = argv[4] if len(argv) > 4 else '27017'

# Load config.ini config vars
config = configparser.ConfigParser()
config.read(repo_dir+'/config.ini')

mongodb_user = config.get('mongodb', 'user')
mongodb_pwd = config.get('mongodb', 'password')