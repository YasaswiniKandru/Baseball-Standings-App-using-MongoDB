from pymongo import MongoClient
import sys
def insert():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]
    collection = db["teams"]

    with open(sys.argv[1], 'r') as my_file:
        data = my_file.read()
    my_file.close()

    list1 = data.split('\n')
    collection.delete_many({})
    final=[]
    for i in list1:
        document={}
        list2 = i.split(':')

        document["name"] = list2[0]
        document["location"] = list2[1]
        document["code"] = list2[2]
        final.append(document)
    seen = set()
    result = [x for x in final if [(x["code"]) not in seen, seen.add((x["code"]))][0]]
    db.teams.insert_many(result)
insert()