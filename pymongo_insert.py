from app import get_database
from scraper import get_persons

dbname = get_database()
collection_name = dbname["artists"]

dataFromScraper = get_persons()


collection_name.insert_many(dataFromScraper)