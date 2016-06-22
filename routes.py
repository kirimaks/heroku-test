from flask import Flask, Response
from scheduler import Scheduler
from proxy_list.get_proxy import GetProxy
import json

app = Flask(__name__)

scheduler = Scheduler()
scheduler.start()


@app.route("/")
def hello():
    pl = GetProxy()

    buff = [pl.get_proxy() for i in range(10)]

    resp = Response(json.dumps(buff), status=200, mimetype="application/json")

    return resp

if __name__ == "__main__":
    app.run()
