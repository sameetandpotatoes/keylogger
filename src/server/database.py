from pymongo import MongoClient
from models.user import User
from models.phrasestroke import PhraseStroke


def setup_database():
    global users, phrases, db, client
    client = MongoClient()
    reset_database()
    db = client['keylogger']
    users = db['users']
    phrases = db['phrases']
    print("DB:")
    print(db)
    print("Value of user:")
    print(users)


def reset_database():
    client.drop_database('keylogger')


def get_user_id(user):
    return users.find_one(user)


def insert_user(user):
    global users
    user_dict = user.__dict__
    return users.insert_one(user_dict)


def insert_phrases(user, phrases_list):
    for p in phrases_list:
        user_id = get_user_id(user.__dict__)
        if user_id is None:
            user_id = insert_user(user)
        phrase = p.__dict__
        phrase['user_id'] = str(user_id)
        phrases.insert_one(phrase)


users, phrases, db, client = None, None, None, None
