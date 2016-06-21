from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello():
    db = sqlite3.connect("mydb")
    cursor = db.cursor()

    return "Hello World!"

if __name__ == "__main__":
    app.run()
