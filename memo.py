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
