from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask('__name__')
CORS(app)

@app.route('/baseball/standings/', methods=['GET'])
def get_standings():
    data = {"standings": []}

    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]

    teams = list(db.teams.find({}, {"_id": 0}))

    games = list(db.games.find({}, {"_id": 0}))

    final = {"standings": []}

    for t in teams:
        r,w,l,d = {},0,0,0


        for g in games:

            if t["code"] == g["v_code"]:

                if int(g["v_score"]) > int(g["h_score"]):
                    w = w + 1
                elif int(g["v_score"]) < int(g["h_score"]):
                    l = l + 1
                else:
                    d = d + 1
            if t["code"] == g["h_code"]:
                if int(g["h_score"]) > int(g["v_score"]):
                    w = w + 1
                elif int(g["h_score"]) < int(g["v_score"]):
                    l = l + 1
                else:
                    d = d + 1
        r["losses"] = l
        r["percent"] = round((w + d * 0.5) / (l + w + d), 3)
        r["tcode"] = t["code"]
        r["ties"] = d
        r["tname"] = t["name"]
        r["wins"] = w

        final["standings"].append(r)
    return final

@app.route('/baseball/results/<string:tcode>/', methods=['GET'])
def ger_result(tcode):

    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]

    teams = list(db.teams.find({}, {"_id": 0}))
    games = list(db.games.find({}, {"_id": 0}))

    final = {"results": []}

    team = tcode
    for g in games:
        l = {}
        if team == g["v_code"]:
            l["gdate"] = g["date"]
            l["opponent"] = g["h_code"]
            l["result"] = "WIN" if int(g["v_score"]) > int(g["h_score"]) else "LOSE" if int(g["v_score"]) < int(g["h_score"]) else "TIE"
            l["them"] = g["h_score"]
            l["us"] = g["v_score"]
            final["results"].append(l)
        if team == g["h_code"]:
            l["gdate"] = g["date"]
            l["opponent"] = g["v_code"]
            l["result"] = "WIN" if int(g["h_score"]) > int(g["v_score"]) else "LOSE" if int(g["h_score"]) < int(g["v_score"]) else "TIE"
            l["them"] = g["v_score"]
            l["us"] = g["h_score"]
            final["results"].append(l)
    for t in teams:
        if team == t["code"]:
            final["tloc"] = t["location"]
            final["tname"] = t["name"]

    return final

if __name__ == '__main__':
    app.run(host='localhost',port=5000)