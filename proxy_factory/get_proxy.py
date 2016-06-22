# -*- coding: utf8 -*-

import json
import sys
import os

tmp_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(tmp_path)

from proxy_list.get_proxy import GetProxy as GetPrx


class GetProxy(object):
    def __init__(self):
        self.pl = GetPrx()

    def get_proxy(self, format, protocol):
        proxy_buff = list()

        if protocol == "https":
            proxy_buff.append(self.pl.get_https_proxy().encode("utf8"))
        else:   # Get with any protocol.
            proxy_buff.append(self.pl.get_proxy().encode("utf8"))

        if format == "plain":
            return proxy_buff

        else:
            return json.dumps(proxy_buff)
