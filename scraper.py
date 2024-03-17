import requests
from bs4 import BeautifulSoup

persons = []

def scraper(url): 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    sourcePage = requests.get(url, headers=headers)
    soup = BeautifulSoup(sourcePage.text, 'html.parser')
    elements = soup.find(class_='wikitable').find_all('tr')[1:]


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
    else:
        name = None

scraper('https://en.wikipedia.org/wiki/List_of_Palestinians#Musicians')

def get_persons():
    return persons