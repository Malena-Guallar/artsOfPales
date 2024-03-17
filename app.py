from pymongo.mongo_client import MongoClient
import certifi
import os
from dotenv import load_dotenv
from flask import Flask, Response, request, jsonify
from bson.json_util import dumps

load_dotenv()

app=Flask(__name__)

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   uri = os.environ.get("MONGO_URI")
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(uri, tlsCAFile=certifi.where())

   try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
   except Exception as e:
    print(e)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['arts_of_Pales']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   

   dbname = get_database()


@app.get("/api/artists")
def get_artists():
  artist_id = request.args.get('_id')
  filter = {} if artist_id is None else {"_id": artist_id}
  artists = list(get_database().artists.find(filter))

  response = Response(
    response = dumps(artists), status = 200, mimetype="application/json")
  return response 