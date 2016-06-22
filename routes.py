from flask import Flask, Response
from scheduler import Scheduler
from proxy_factory.get_proxy import GetProxy
from proxy_factory.get_proxy_list import GetProxyList

app = Flask(__name__)

scheduler = Scheduler()
scheduler.start()


def get_mime(format):
    mime = ("text/plain"
            if format == "plain"
            else "application/json; charset=utf-8")
    return mime


@app.route("/")
def hello():
    return "Hello world"


@app.route("/get_proxy_list")
@app.route("/get_proxy_list/<format>")
@app.route("/get_proxy_list/<format>/<int:number>")
@app.route("/get_proxy_list/<format>/<int:number>/<protocol>")
def proxy_list(format="plain", number=10, protocol=None):
    proxy_factory = GetProxyList()
    buff = proxy_factory.get_proxy_list(format, number, protocol)
    return Response(buff, mimetype=get_mime(format), status=200)


@app.route("/get_proxy")
@app.route("/get_proxy/<format>")
@app.route("/get_proxy/<format>/<protocol>")
def get_proxy(format="plain", protocol=None):
    proxy_factory = GetProxy()
    buff = proxy_factory.get_proxy(format, protocol)
    return Response(buff, mimetype=get_mime(format), status=200)


if __name__ == "__main__":
    app.run()
