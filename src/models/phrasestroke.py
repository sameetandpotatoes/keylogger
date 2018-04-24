from datetime import datetime
import dateutil.parser
import json

class PhraseStroke:
    def __init__(self, start_time, phrase, terminating, end_time=datetime.now(),
                copy_pastaed=False):
        self.end_timestamp = str(end_time)
        self.start_timestamp = str(start_time)
        self.duration = (dateutil.parser.parse(self.end_timestamp) - dateutil.parser.parse(self.start_timestamp)).total_seconds()
        self.phrase = phrase
        self.terminating = terminating
        self.copy_pastaed = copy_pastaed

    @classmethod
    def from_json(cls, jd):
        return cls(jd['start_timestamp'], jd['phrase'], jd['terminating'], jd['end_timestamp'], jd['copy_pastaed'])
