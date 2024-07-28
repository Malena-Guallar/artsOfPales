import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

def scraper(url): 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        source_page = requests.get(url, headers=headers)
        source_page.raise_for_status() # raise error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url} : {e}")
        return []
    
    soup = BeautifulSoup(source_page.text, 'html.parser')
    elements = soup.find(class_='wikitable').find_all('tr')[1:]

    persons = []


    for element in elements:
        name = element.find('a')
        if name is not None:
            fullname = name.text.split(' ')
            firstname = fullname[0]
            lastname = ' '.join(fullname[1:])
            field = element.find('td').find_next_sibling('td')
            new_person = {"firstname": firstname, "lastname": lastname, "field": field.text}
            if "Politics" not in field.text and "Academic" not in field.text and "Academia" not in field.text and "Business" not in field.text and "Medicine" not in field.text and "Religion" not in field.text and "Sport" not in field.text:
                persons.append(new_person)
    return persons
    # else:
    #     name = None

def save_to_db(persons, collection_name):
    uri = os.environ.get("MONGO_URI")
    client = MongoClient(uri, tlsCAFile=certifi.where())
    db = client['arts_of_Pales']
    collection = db[collection_name]
    collection.insert_many(persons)

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_Palestinians#Musicians'
    persons = scraper(url)
    if persons:
        save_to_db(persons, 'artists')