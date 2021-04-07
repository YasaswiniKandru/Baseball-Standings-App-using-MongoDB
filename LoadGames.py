from pymongo import MongoClient
import sys
def insert():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]
    collection = db["games"]

    with open(sys.argv[1], 'r') as my_file:
        data = my_file.read()
    my_file.close()
    teams_list = db.teams.find({},{"code":1, "_id":0}).distinct("code")
    list1 = data.split('\n')
    collection.delete_many({})
    final =[]
    for i in list1:
        document={}
        list2 = i.split(':')
        document["date"] = list2[0]
        document["v_code"] = list2[1]
        document["h_code"] = list2[2]
        document["v_score"] = list2[3]
        document["h_score"] = list2[4]
        if document["v_code"] not in teams_list or document["h_code"] not in teams_list:
            continue
        else:
            final.append(document)
    db.games.insert_many(final)
insert()