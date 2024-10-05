import keyboard

class InputManager:
    def __init__(self):
        self.arrow_input = [0, 0]
        self.space_pressed = False
        self.shift_pressed = False
        
        keyboard.on_press_key("left", self.on_left_arrow_press)
        keyboard.on_press_key("right", self.on_right_arrow_press)
        keyboard.on_press_key("up", self.on_up_arrow_press)
        keyboard.on_press_key("down", self.on_down_arrow_press)
        keyboard.on_press_key("space", self.on_space_press)
        keyboard.on_press_key("shift", self.on_shift_press)

        keyboard.on_release_key("left", self.on_left_arrow_release)
        keyboard.on_release_key("right", self.on_right_arrow_release)
        keyboard.on_release_key("up", self.on_up_arrow_release)
        keyboard.on_release_key("down", self.on_down_arrow_release)
        keyboard.on_release_key("space", self.on_space_release)
        keyboard.on_release_key("shift", self.on_shift_release)

    def on_left_arrow_press(self):
        self.arrow_input[0] -= 1

    def on_right_arrow_press(self):
        self.arrow_input[0] += 1

    def on_up_arrow_press(self):
        self.arrow_input[1] += 1

    def on_down_arrow_press(self):
        self.arrow_input[1] -= 1

    def on_left_arrow_release(self):
        self.arrow_input[0] += 1

    def on_right_arrow_release(self):
        self.arrow_input[0] -= 1

    def on_up_arrow_release(self):
        self.arrow_input[1] -= 1

    def on_down_arrow_release(self):
        self.arrow_input[1] += 1

    def on_space_press(self):
        self.space_pressed = True

    def on_space_release(self):
        self.space_pressed = False

    def on_shift_press(self):
        self.shift_pressed = True

    def on_shift_release(self):
        self.shift_pressed = False