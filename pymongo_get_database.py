from pymongo.mongo_client import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   uri = os.environ.get("MONGO_URI")
   print(uri)
 
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

