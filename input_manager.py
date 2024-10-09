import keyboard

class InputManager:
    def __init__(self):
        self.arrow_input = [0, 0]
        self.space_pressed = False
        self.shift_pressed = False
        self.z_pressed = False
        self.x_pressed = False
        
        keyboard.on_left_arrow_press.subscribe(self.on_left_arrow_press)
        keyboard.on_right_arrow_press.subscribe(self.on_right_arrow_press)
        keyboard.on_up_arrow_press.subscribe(self.on_up_arrow_press)
        keyboard.on_down_arrow_press.subscribe(self.on_down_arrow_press)
        keyboard.on_space_press.subscribe(self.on_space_press)
        keyboard.on_shift_press.subscribe(self.on_shift_press)
        keyboard.on_z_press.subscribe(self.on_z_press)
        keyboard.on_x_press.subscribe(self.on_x_press)

        keyboard.on_left_arrow_release.subscribe(self.on_left_arrow_release)
        keyboard.on_right_arrow_release.subscribe(self.on_right_arrow_release)
        keyboard.on_up_arrow_release.subscribe(self.on_up_arrow_release)
        keyboard.on_down_arrow_release.subscribe(self.on_down_arrow_release)
        keyboard.on_space_release.subscribe(self.on_space_release)
        keyboard.on_shift_release.subscribe(self.on_shift_release)
        keyboard.on_z_release.subscribe(self.on_z_release)
        keyboard.on_x_release.subscribe(self.on_x_release)

    def on_left_arrow_press(self):
        self.arrow_input[0] = -1

    def on_right_arrow_press(self):
        self.arrow_input[0] = 1

    def on_up_arrow_press(self):
        self.arrow_input[1] = 1

    def on_down_arrow_press(self):
        self.arrow_input[1] = -1

    def on_left_arrow_release(self):
        self.arrow_input[0] = 0

    def on_right_arrow_release(self):
        self.arrow_input[0] = 0

    def on_up_arrow_release(self):
        self.arrow_input[1] = 0

    def on_down_arrow_release(self):
        self.arrow_input[1] = 0

    def on_space_press(self):
        self.space_pressed = True

    def on_space_release(self):
        self.space_pressed = False

    def on_shift_press(self):
        self.shift_pressed = True

    def on_shift_release(self):
        self.shift_pressed = False
        
    def on_z_press(self):
        self.z_pressed = True
        
    def on_z_release(self):
        self.z_pressed = False
        
    def on_x_press(self):
        self.x_pressed = True
        
    def on_x_release(self):
        self.x_pressed = False