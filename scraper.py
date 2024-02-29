import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

sourcePage = requests.get('https://en.wikipedia.org/wiki/List_of_Palestinians#Musicians', headers=headers)

soup = BeautifulSoup(sourcePage.text, 'html.parser')

elements = soup.find(class_='wikitable').find_all('tr')

persons = []

for element in elements:
    name = element.find('a')
    if name is not None:
        field = element.find('td').find_next_sibling('td')
        new_person = {"name": name.text, "field": field.text}
        if "Politics" not in field.text and "Academic" not in field.text and "Academia" not in field.text and "Business" not in field.text and "Medicine" not in field.text and "Religion" not in field.text and "Sport" not in field.text:
            persons.append(new_person)
    else:
        name = None
print(persons)

# here I need to convert unicode strings to regular ascii strings because python2 does not support unicode natively.        
#converted_persons = [{key: value.encode('utf-8') if isinstance(value, unicode) else value for key, value in person.items()} for person in persons]

def get_all_persons():
    return persons