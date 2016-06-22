import threading
import time
from random import randrange
from ConfigParser import ConfigParser
import sqlite3


class Scheduler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        config = ConfigParser()
        config.read("config.cfg")
        self.db_file = config.get("Database", "file")

    def run(self):
        while True:
            conn = sqlite3.connect(self.db_file)
            with conn:
                cursor = conn.cursor()
                query = """
                    INSERT INTO data(number) VALUES(?)
                """

                rnum = randrange(0, 1000)

                cursor.execute(query, (rnum,))

            time.sleep(10)
