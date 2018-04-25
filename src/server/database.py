import os
from pymongo import MongoClient


def setup_database():
    global db, client

    MONGO_URL = os.environ.get('MONGOHQ_URL')
    if MONGO_URL:
        # Heroku
        client = MongoClient(MONGO_URL)
    else:
        # Local (Development)
        client = MongoClient()
        reset_database()

    db = client['keylogger']


def reset_database():
    client.drop_database('keylogger')


def get_user_id(user):
    # TODO Andrew: should we not store the image, and just store tags? and query by mac address
    return db.users.find_one(user)


def get_users_by_os(os):
    return db.users.find({"os":os})


def get_copied_phrases(n=100):
    # TODO Andrew: do group by phrase, and aggregate count, and limit to first n
    return db.phrases.find({"copy_pastaed": True})


def insert_user(user):
    user_dict = user.__dict__
    return db.users.insert_one(user_dict)


def insert_phrases(user, phrases_list):
    for p in phrases_list:
        user_id = get_user_id(user.__dict__)
        if user_id is None:
            user_id = insert_user(user)
        phrase = p.__dict__
        phrase['user_id'] = str(user_id)
        db.phrases.insert_one(phrase)


db, client = None, None
