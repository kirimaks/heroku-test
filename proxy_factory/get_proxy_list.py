import json


class GetProxyList(object):
    def __init__(self):
        pass

    def get_proxy_list(self, format, number):
        return "Proxy list, format: [%s], number: [%s]" % (format, number)
