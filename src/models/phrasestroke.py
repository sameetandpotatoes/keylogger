from datetime import datetime
import dateutil.parser
import json

class PhraseStroke:
    def __init__(self, phrase, terminating, start_time=datetime.now(), end_time=datetime.now(), copy_pastaed=False):
        # Required parameters
        self.phrase = phrase
        self.terminating = terminating
        # Optional parameters
        self.start_timestamp = str(start_time)
        self.end_timestamp = str(end_time)
        try:
            self.duration = (dateutil.parser.parse(self.end_timestamp) - dateutil.parser.parse(self.start_timestamp)).total_seconds()
        except ValueError:
            self.duration = 0
        self.copy_pastaed = copy_pastaed

    @classmethod
    def from_json(cls, jd):
        return cls(jd['phrase'], jd['terminating'], jd['start_timestamp'], jd['end_timestamp'], jd['copy_pastaed'])
