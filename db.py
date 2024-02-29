import sqlite3

connection = sqlite3.connect('pales.db')
c = connection.cursor()

#c.execute('''CREATE TABLE artists(id INT, firstname TEXT, lastname TEXT, field TEXT)''')

c.execute('''SELECT * FROM artists''')
results = c.fetchall()
print(results)