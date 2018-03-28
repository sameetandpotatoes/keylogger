import datetime


class KeyPress:
    def __init__(self, key):
        self.timestamp = datetime.datetime.now()
        self.key = key

    def __str__(self):
        return '{}: {}'.format(self.timestamp, self.key)
