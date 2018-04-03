import datetime
import json
import IPython

class PhraseStroke:
    def __init__(self, start_timestamp, phrase, ending_character):
        self.end_timestamp = str(datetime.datetime.now())
        self.start_timestamp = start_timestamp
        self.phrase = phrase
        self.terminating = ending_character
