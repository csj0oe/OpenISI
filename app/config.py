import os

# Define repo dir
repo_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../'))

# Define server host
host = argv[1] if len(argv) > 1 else 'localhost'

# Define server port
port = int(argv[2]) if len(argv) > 2 else 8080

# Define mongodb host
mongodb_host = argv[3] if len(argv) > 3 else 'localhost'

# Define mongodb port
mongodb_port = argv[4] if len(argv) > 4 else '27017'

# Define mongodb user
mongodb_user = argv[5] if len(argv) > 5 else 'user'

# Define mongodb password
mongodb_pwd = argv[6] if len(argv) > 6 else 'password'