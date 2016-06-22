from flask import Flask, Response
from scheduler import Scheduler
from proxy_factory.get_proxy import GetProxy
from proxy_factory.get_proxy_list import GetProxyList

app = Flask(__name__)

scheduler = Scheduler()
scheduler.start()


def get_mime(format):
    return "text/plain" if format == "plain" else "application/json"


@app.route("/")
def hello():
    return "Hello world"


@app.route("/get_proxy_list/<format>/<number>")
def proxy_list(number=10, format="plain"):
    proxy_factory = GetProxyList()
    buff = proxy_factory.get_proxy_list(format, number)
    return Response(buff, mimetype=get_mime(format), status=200)


@app.route("/get_proxy/<format>")
def get_proxy(format="plain"):
    proxy_factory = GetProxy()
    buff = proxy_factory.get_proxy(format)
    return Response(buff, mimetype=get_mime(format), status=200)


if __name__ == "__main__":
    app.run()
