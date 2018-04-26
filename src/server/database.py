import os
from pymongo import MongoClient
from utils import database as get_db

def setup_database():
    global db, client

    MONGO_URL = get_db.get_database_credentials()
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


def insert_user(user):
    user_dict = user.__dict__
    print("Inserting")
    print(user_dict.keys())
    return db.users.insert_one(user_dict)


def insert_phrases(user, phrases_list):
    for p in phrases_list:
        user_id = get_user_id(user.__dict__)
        if user_id is None:
            print("Bad user id")
        phrase = p.__dict__
        print("Val of cp:")
        print(phrase["copy_pastaed"])
        phrase['user_id'] = str(user_id)
        db.phrases.insert_one(phrase)


def update_user(user):
    db.users.update({"mac": user.mac}, {"$set": user}, upsert=False)


db, client = None, None
