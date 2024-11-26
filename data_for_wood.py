import sqlite3
from time import strftime
from datetime import datetime

conn = sqlite3.connect('wood_calculator.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS wood_calculator
            (name TEXT, date TEXT, measurement REAL, total_number_boards REAL)''')
conn.commit()
conn.close()


date2 = datetime.now().strftime(f"%d-%m-%Y | %H:%M:%S %p")  # Get current date

 
name = "Codewith-Ese".title() 
date = date2
measurement = 0
total_number_boards = 0

            # measurement = phone_ent.get()
conn = sqlite3.connect('wood_calculator.db')
c = conn.cursor()
c.execute("INSERT INTO wood_calculator (name, date, measurement, total_number_boards) VALUES (?, ?, ?, ?)", (name, date, measurement, total_number_boards))
conn.commit()
conn.close()

#  Reading from my data base 
conn = sqlite3.connect('wood_calculator.db')
c = conn.cursor()
c.execute("SELECT * FROM wood_calculator")
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)
    

