import sqlite3
# Создание SQL-базы данных
conn = sqlite3.connect('database.db')  #
cur = conn.cursor()  #

# Создание таблицы
cur.execute('CREATE TABLE IF NOT EXISTS users(\n'
            'userid INT PRIMARY KEY,\n'
            'fname TEXT,\n'
            'lname TEXT,\n'
            'gender TEXT);\n')
conn.commit()  # Сохранение изменений


cur.execute('CREATE TABLE IF NOT EXISTS orders(\n'
            'orderid INT PRIMARY KEY,\n'
            'date TEXT,\n'
            'userid TEXT,\n'
            'total TEXT);\n')
conn.commit()

# Добавление данных (небезопасный способ)
cur.execute("""INSERT INTO users(userid, fname, lname, gender)
            VALUES('00001', 'Ilya', 'Solovyov', 'male');""")
conn.commit()

# Добавление данных из кортежа
new_user = ('00002', 'Beth', 'Solovyova', 'female')
cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", new_user)
conn.commit()


# Добавление данных из нескольких кортежей
users = [('00002', 'Beth', 'Solovyova', 'female'), ('00001', 'Ilya', 'Solovyov', 'male')]
cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", users)
conn.commit()



# Получение данных из таблицы
cur.execute("SELECT * FROM users")
result = cur.fetchone()
print(result)

# Получение нескольких кортежей из таблицы
cur.execute("SELECT * FROM users")
result = cur.fetchmany(2)
print(result)

#  Получение всех кортежей из таблицы
cur.execute("SELECT * FROM users")
result = cur.fetchall()
print(result)


#  Удаление данных из таблицы
cur.execute("DELETE FROM users WHERE fname='Beth';")
conn.commit()
