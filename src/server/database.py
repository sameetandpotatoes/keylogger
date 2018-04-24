from pymongo import MongoClient


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
    # TODO Andrew: should we not store the image, and just store tags? and query by mac address (that's there now)
    return users.find_one(user)


def get_users_by_os(os):
    return users.find({"os":os})


def get_copied_phrases(n=100):
    # TODO Andrew: do group by phrase, and aggregate count, and limit to first n
    return phrases.find({"copy_pastaed": True})


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
