from pynput import keyboard

class KeyboardController:
    def __init__(self):
        self.keys = {
            'up': False,
            'down': False,
            'left': False,
            'right': False,
            'shift': False,
            'space': False,
            'f': False,
            'j': False
        }
        self.listener = keyboard.Listener(
            on_press=self._set_key_down,
            on_release=self._set_key_up)
        self.listener.start()

    def _set_key_down(self, key):
        key_name = str(key).replace("'", "")
        if key_name in self.keys:
            self.keys[key_name] = True

    def _set_key_up(self, key):
        key_name = str(key).replace("'", "")
        if key_name in self.keys:
            self.keys[key_name] = False

    def is_key_pressed(self, key):
        return self.keys.get(key, False)
