import yaml

DEBUG=True

def get_database_credentials():
    mongo = yaml.load(open('src/config/database.yaml'))['mongo']
    return "mongodb://{}:{}@{}/{}".format(mongo['username'], mongo['password'], mongo['host'], mongo['db_name'])
