import sqlite3
import os.path


class db_desc_test(object):
    def __init__(self):
        self.db = sqlite3.connect("mydb")
        self.cursor = self.db.cursor()

        query = """
            CREATE TABLE IF NOT EXISTS data(
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                number  INTEGER NOT NULL
            )
        """

        self.cursor.execute(query)
        self.db.commit()

    def __del__(self):
        self.db.close()

    def __set__(self, obj, value):
        num = value
        query = """
            INSERT INTO data(number) VALUES(?)
        """
        print(query)
        self.cursor.execute(query, (num,))
        self.db.commit()

    def __get__(self, obj, objtype):
        query = """
            SELECT * from data
        """
        print(query)
        self.cursor.execute(query)
        buff = self.cursor.fetchall()
        print(buff)
        return buff


class db_test(object):
    num = db_desc_test()
