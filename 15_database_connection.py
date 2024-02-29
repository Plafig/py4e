import sqlite3

db_path = "C:\\Users\\Oleksandr_Kuzianin\\Desktop\\py4e.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')
conn.close()