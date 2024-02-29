## With SQLite, data is on the client terminal and not on distant server. 

import sqlite3
from scraper import get_persons

# DB creation
connection = sqlite3.connect('pales.db')
c = connection.cursor()

# Table creation
#c.execute('''CREATE TABLE artists(id INT, firstname TEXT, lastname TEXT, field TEXT)''')

dataFromScraper = get_persons()

# Inserting data to db from scraper
def insertInDb(data):
    for person in data:
        id = person["id"]
        firstname = person["firstname"]
        lastname = person["lastname"]
        field = person["field"]
        c.execute(''' INSERT INTO artists VALUES (?,?,?,?)''', (id, firstname, lastname, field))

#insertInDb(dataFromScraper)
# connection.commit()
# print('complete')

# c.execute('''SELECT * FROM artists''')
# results = c.fetchall()
# connection.commit()
# print(results)

# c.execute('''DELETE from artists''')
# results = c.fetchall()
# connection.commit()
# print(results)

connection.close()