# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
from scraper import get_persons

dbname = get_database()
collection_name = dbname["artists"]

dataFromScraper = get_persons()

item1 = {
    "name": "pistache",
    "field": 'art'
}

collection_name.insert_many(dataFromScraper)