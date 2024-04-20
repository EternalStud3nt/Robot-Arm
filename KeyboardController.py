import keyboard

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
        for key in self.keys:
            keyboard.on_press_key(key, self._set_key_down, suppress=False)
            keyboard.on_release_key(key, self._set_key_up, suppress=False)

    def _set_key_down(self, e):
        if e.name in self.keys:
            self.keys[e.name] = True

    def _set_key_up(self, e):
        if e.name in self.keys:
            self.keys[e.name] = False

    def is_key_pressed(self, key):
        return self.keys.get(key, False)

