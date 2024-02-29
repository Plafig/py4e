import sqlite3

conn = sqlite3.connect("C:\\Users\\Oleksandr_Kuzianin\\Desktop\\py4e.db")
curr = conn.cursor()
curr.execute('DROP TABLE IF EXISTS Track ')
curr.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')
curr.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
curr.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('My Way', 15))
conn.commit()

print("Track: ")
curr.execute('SELECT title, plays FROM Track')
for line in curr:
    print(line)

curr.execute('DELETE FROM Track WHERE plays < 100')

conn.commit()
conn.close