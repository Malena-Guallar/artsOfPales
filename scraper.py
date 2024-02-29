import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

sourcePage = requests.get('https://en.wikipedia.org/wiki/List_of_Palestinians#Musicians', headers=headers)

soup = BeautifulSoup(sourcePage.text, 'html.parser')

elements = soup.find(class_='wikitable').find_all('tr')[1:]

persons = []


for element in elements:
    name = element.find('a')
    if name is not None:
        fullname = name.text.split(' ')
        firstname = fullname[0]
        lastname = ' '.join(fullname[1:])
        field = element.find('td').find_next_sibling('td')
        new_person = {"index": 0, "firstname": firstname, "lastname": lastname, "field": field.text}
        if "Politics" not in field.text and "Academic" not in field.text and "Academia" not in field.text and "Business" not in field.text and "Medicine" not in field.text and "Religion" not in field.text and "Sport" not in field.text:
            persons.append(new_person)
    else:
        name = None

for person in persons:  
    index = persons.index(person)
    person["index"] = index
    

def get_all_persons():  
    return persons