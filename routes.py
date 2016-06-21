from flask import Flask
from db_test import db_test
from random import randrange

app = Flask(__name__)
my_db = db_test()

my_db.num = randrange(0, 100)


@app.route("/")
def hello():
    out = my_db.num
    return str(out)

if __name__ == "__main__":
    app.run()
