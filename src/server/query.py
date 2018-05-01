from server import database

def get_users_by_os(os):
    return database.db.users.find({"os": os})


def get_copied_phrases(n=100):
    pipeline = [
        {"$unwind": "$phrases"},
        {"$match": {"phrases.copy_pastaed": True}},
        {"$group": {"_id":"$phrases.phrase", "num": {"$sum":1}, "user_ip": {"$addToSet": "$ip"}}},
        {"$limit": int(n)},
        {"$project": {"_id": 0, "phrase": "$_id", "user_ip": 1, "num_occurences":"$num"}}
    ]
    return database.db.users.aggregate(pipeline)
