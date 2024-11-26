import sqlite3
from time import strftime
from datetime import datetime

conn = sqlite3.connect('ese_savings2.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ese_savings2
            (name TEXT, date TEXT, savings REAL, income REAL)''')
conn.commit()
conn.close()


date2 = datetime.now().strftime(f"%d-%m-%Y------- %H:%M:%S %p")  # Get current date

 
name = "monday eseinone".title() 
date = date2
savings = 0
income = 0

            # savings = phone_ent.get()
conn = sqlite3.connect('ese_savings2.db')
c = conn.cursor()
c.execute("INSERT INTO ese_savings2 (name, date, savings, income) VALUES (?, ?, ?, ?)", (name, date, savings, income))
conn.commit()
conn.close()

#  Reading from my data base 
conn = sqlite3.connect('ese_savings2.db')
c = conn.cursor()
c.execute("SELECT * FROM ese_savings2")
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)
    

