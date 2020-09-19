import sqlite3

URL = "Z:\sqlite\db\sqlitedb"

class Connection:
    def __init__(self, url = URL):
        self.connection = sqlite3.connect(url)

    def __get_cursor(self):
        return self.connection.cursor()

    def execute(self, query):
        cursor = self.__get_cursor()
        cursor.execute(query)
        self.connection.commit()
        return cursor.fetchall()

    def execute_many(self, query):
        cursor = self.__get_cursor()
        cursor.executescript(query)
        self.connection.commit()
        return cursor.fetchall()

    def close(self):
        self.connection.close()

    def __del__(self):
        self.close()
#