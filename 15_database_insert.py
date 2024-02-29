import sqlite3

conn = sqlite3.connect("C:\\Users\\Oleksandr_Kuzianin\\Desktop\\py4e.db")
curr = conn.cursor()
curr.execute('DROP TABLE IF EXISTS Track ')
curr.execute('CREATE TABLE Track')
curr.execute('INSERT INTO Track ()')

