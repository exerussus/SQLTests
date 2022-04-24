

class Identification:

    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXIST users(
                            userid INT PRIMARY KEY,
                            login TEXT,
                            password TEXT,
                            );""")

    def entry(self):
        pass

    def login(self):
        pass

    def registration(self):
        pass
