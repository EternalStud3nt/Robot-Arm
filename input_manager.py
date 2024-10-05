import keyboard

class InputManager:
    def __init__(self):
        self.arrow_input = [0, 0]
        
        keyboard.on_press_key("left", self.on_left_arrow_press)
        keyboard.on_press_key("right", self.on_right_arrow_press)
        keyboard.on_press_key("up", self.on_up_arrow_press)
        keyboard.on_press_key("down", self.on_down_arrow_press)

        keyboard.on_release_key("left", self.on_left_arrow_release)
        keyboard.on_release_key("right", self.on_right_arrow_release)
        keyboard.on_release_key("up", self.on_up_arrow_release)
        keyboard.on_release_key("down", self.on_down_arrow_release)

    def on_left_arrow_press(self, event):
        self.arrow_input[0] -= 1

    def on_right_arrow_press(self, event):
        self.arrow_input[0] += 1

    def on_up_arrow_press(self, event):
        self.arrow_input[1] += 1

    def on_down_arrow_press(self, event):
        self.arrow_input[1] -= 1

    def on_left_arrow_release(self, event):
        self.arrow_input[0] += 1

    def on_right_arrow_release(self, event):
        self.arrow_input[0] -= 1

    def on_up_arrow_release(self, event):
        self.arrow_input[1] -= 1

    def on_down_arrow_release(self, event):
        self.arrow_input[1] += 1