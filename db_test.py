import sqlite3


class db_test(object):
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
        self.cursor.execute(query, (num,))
        self.db.commit()

    def __get__(self, obj, objtype):
        query = """
            SELECT * from data
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
