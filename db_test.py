import sqlite3
from ConfigParser import ConfigParser


class db_desc_test(object):
    def __init__(self):
        # Get database name.
        config = ConfigParser()
        config.read("config.cfg")
        self.db_name = config.get("Database", "file")

        # Create table if need.
        conn = sqlite3.connect(self.db_name)
        with conn:
            cursor = conn.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS data(
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    number  INTEGER NOT NULL
                )
            """
            cursor.execute(query)

    def __set__(self, obj, value):
        conn = sqlite3.connect(self.db_name)
        with conn:
            cursor = conn.cursor()
            num = value
            query = """
                INSERT INTO data(number) VALUES(?)
            """
            print(query)
            cursor.execute(query, (num,))

    def __get__(self, obj, objtype):
        conn = sqlite3.connect(self.db_name)
        with conn:
            cursor = conn.cursor()
            query = """
                SELECT * from data
            """
            print(query)
            cursor.execute(query)
            buff = cursor.fetchall()

        print(buff)
        return buff


class db_test(object):
    num = db_desc_test()
