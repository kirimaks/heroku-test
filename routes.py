from flask import Flask
from db_test import db_test
# from random import randrange
from scheduler import Scheduler

app = Flask(__name__)
my_db = db_test()

scheduler = Scheduler()
scheduler.start()


@app.route("/")
def hello():
    out = my_db.num
    return str(out)

if __name__ == "__main__":
    app.run()
