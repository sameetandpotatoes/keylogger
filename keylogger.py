from pynput.keyboard import Key, Listener
from keypress import KeyPress

class KeyListener:
    BUFFER_CAPACITY = 50

    def __init__(self):
        self.buffered_keys = []
        with Listener(on_press=on_press) as listener:
            listener.join()

    def on_press(key):
        self.buffered_keys.push('"{0}"'.format(key))

        if len(self.buffered_keys) >= BUFFER_CAPACITY:
            # Flush buffer

            self.buffered_keys = []


def main():
    KeyListener()

if __name__ == '__main__':
    main()
