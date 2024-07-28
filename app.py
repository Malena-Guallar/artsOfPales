from pymongo.mongo_client import MongoClient
import certifi
import os
from dotenv import load_dotenv
from flask import Flask, Response, request, jsonify
from bson.json_util import dumps, ObjectId
from pydantic import ValidationError

from model import Artist

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

@app.errorhandler(404)
def resource_not_found(error):
   return jsonify(f"{error} : Not found"), 404

@app.errorhandler(500)
def internal_error(error):
   return jsonify(f"{error} : Internal server error"), 500


@app.get("/api/artists")
def get_artists():
   try:
    db= get_database()
    artists = list(db.artists.find())
    return Response(dumps(artists), status=200, mimetype="application/json")
   except Exception as e:
      return jsonify({"error": str(e)}), 500

@app.get("/api/artist/<artist_id>")
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

@app.post("/api/artist")
def post_artist():
    try:
        data = request.json
        artist = Artist(**data)

        db = get_database()
        result = db.artists.insert_one(artist.model_dump(by_alias=True))  # Utilisez by_alias pour gérer `_id`
        return jsonify({"message": f"CREATE: {artist.firstname} was added to the collection", "id": str(result.inserted_id)}), 201

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":   

   db = get_database()
   app.run(debug=True)