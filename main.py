import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()


cur.execute("SELECT * FROM users")
result = cur.fetchall()
print(result)



cur.execute("SELECT * FROM users")
result = cur.fetchall()
print(result)
