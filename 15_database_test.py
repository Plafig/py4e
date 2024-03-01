import sqlite3
db_path = 'C:\\Users\\Oleksandr_Kuzianin\\Desktop\\py4e.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Laptops')
cur.execute('CREATE TABLE Laptops (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, model VARCHAR(25), price INTEGER)')
cur.execute('INSERT INTO Laptops (model, price) VALUES (?, ?)', ('HP', 1200))
conn.commit()
conn.close