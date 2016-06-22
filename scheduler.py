import threading
import time
import os


class Scheduler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            os.system("python proxy_list/create_proxy_list.py")
            time.sleep(100)
