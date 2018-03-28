from pynput.keyboard import Key, Listener
from keypress import KeyPress


class KeyListener:
    BUFFER_CAPACITY = 50

    def __init__(self):
        self.buffered_keys = []

    def run(self):
        with Listener(on_press=lambda key: self.on_press(key)) as listener:
            listener.join()

    def on_press(self, key):
        self.buffered_keys.append(KeyPress(str(key)))
        if len(self.buffered_keys) >= self.BUFFER_CAPACITY:
            # Flush buffer
            self.buffered_keys = []


def main():
    key_listener = KeyListener()
    key_listener.run()


if __name__ == '__main__':
    main()
