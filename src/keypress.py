import datetime
import json

class KeyPress:
    def __init__(self, key):
        self.timestamp = str(datetime.datetime.now())
        self.key = key
