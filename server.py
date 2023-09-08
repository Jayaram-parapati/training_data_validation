from bson import ObjectId
from flask import Flask, render_template, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['training_db']
ents = db['mix_entities']
errors = db['errors']
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/td", methods=["GET", "POST"])
# def getID():
#     ent = list(ents.find({"docbin":False}))
#     txtArray = []
#     entitesArray = []
#     dict = {}


#     for i in ent:
#         text = i["text"]
#         txtArray.append(text)
#         entities = i["entities"]
#         entitesArray.append(entities)

#     dict.update()
#     return jsonify(txtArray)
    

@app.route("/td/<id>")
def getTD(id):
    ent = ents.find_one({"_id":ObjectId(id)},{"_id":0})
    return ent

@app.route("/tdbyindex/<int:index>")
def getTDByIndex(index):
    ent = ents.find({"docbin":False},{"_id":0}).limit(1).skip(index)
    return jsonify(list(ent))


if __name__ == "__main__":
    app.run(debug=True, port=8080)