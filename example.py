import sqlite3


#establish a connection and cursor
connection = sqlite3.connect("dataa.db")
cursor = connection.cursor()

#Query
cursor.execute("SELECT band,date FROM events WHERE band='Trigers'")
rows = cursor.fetchall()
print(rows)

#insert new rows

new_rows = [('Cats', 'Cat City', '2088.10.20'),('Hens', 'Hen City', '2088.10.20')]

cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
connection.commit()