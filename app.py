from pymongo.mongo_client import MongoClient
import certifi
import os
from dotenv import load_dotenv
from flask import Flask, Response, request, jsonify
from bson.json_util import dumps, ObjectId
import json

load_dotenv()

app=Flask(__name__)

def get_database():
    uri = os.environ.get("MONGO_URI")
    client = MongoClient(uri, tlsCAFile=certifi.where())
    try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
      print(e)
    return client['arts_of_Pales']


@app.get("/api/artists")
def get_artists():
   db= get_database()
   artists = list(db.artists.find())
   return Response(dumps(artists), status=200, mimetype="application/json")

# def get_artists():
#   artist_id = request.args.get('_id')
#   filter = {} if artist_id is None else {"_id": artist_id}
#   artists = list(get_database().artists.find(filter))

#   list_of_artists = Response(
#     response = dumps(artists), status = 200, mimetype="application/json")
#   return list_of_artists 

# @app.post("/api/artist")
# def post_artist():
#   firstname = request.args.get("firtsname")
#   lastname = request.args.get("lastname")
#   field = request.args.get("field")

#   dbname = get_database()
#   collection = dbname["artists"]
#   collection.insert_one({"firstname" : firstname, "lastname": lastname, "field": field})
#   return f"CREATE : {firstname} was added to collection" 

@app.get("/api/artists/<artist_id>")
def get_artist(artist_id):
  db = get_database()
  try:
    artist = db.artists.find_one({"_id": ObjectId(artist_id)})
    if artist:
       return Response(dumps(artist), status=200, mimetype="application/json")
    else :
        return jsonify({"error" : "Artist not found"}), 404
  except Exception as e :
      return jsonify({"error" : str(e)}), 400


if __name__ == "__main__":   

   db = get_database()
   app.run(debug=True)