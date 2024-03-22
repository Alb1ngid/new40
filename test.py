import sqlite3
conn = sqlite3.connect('base.db')

cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
age INT DEFAULT 18,
name TEXT NOT NULL
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS games(
id INTEGER NOT NULL,
score INT DEFAULT 0,
times INTEGER 
)''')


cur.execute('''SELECT * FROM users''')
for row in cur.fetchall():
    print(row)
print('------___------')
# cur.execute('''SELECT avg(score) FROM games WHERE id = 1''')
#
# for row1 in cur.fetchall():
#     print(row1)

cur.execute('''SELECT * FROM games''')
for row1 in cur.fetchall():
    print(row1)
print('----------------')

cur.execute('''SELECT user_id,name,age,games.score From games 
LEFT JOIN users ON games.id=users.user_id ORDER BY games.score DESC''')

for row1 in cur.fetchall():
    print(row1)












conn.commit()
conn.close()