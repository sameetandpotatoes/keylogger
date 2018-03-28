""" A class to record a key press """
class KeyPress(self):
    def __init__(self, timestamp, key):
        self.timestamp = timestamp
        self.key = key

    def __str__(self):
        return '{}: {}'.format(self.timestamp, self.key)
