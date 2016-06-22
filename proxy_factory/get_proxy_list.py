# -*- coding: utf8 -*-

import json
import sys
import os

tmp_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(tmp_path)

from proxy_list.get_proxy import GetProxy as GetPrx


class GetProxyList(object):
    def __init__(self):
        self.pl = GetPrx()

    def get_proxy_list(self, format, number):
        proxy_buff = [self.pl.get_proxy() for i in range(number)]

        if format == "plain":
            return str.join(",", proxy_buff)
        else:
            return json.dumps(proxy_buff, indent=4, sort_keys=True)

if __name__ == "__main__":
    test = GetProxyList()
    out = test.get_proxy_list("plain", 10)
    print(out)
    out = test.get_proxy_list("json", 10)
    print(out)
