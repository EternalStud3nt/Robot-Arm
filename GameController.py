import pygame
import time

class GameController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        # Initialize joystick axes
        self.axes = {
            'left_joystick_horizontal': 0,
            'left_joystick_vertical': 0,
            'right_joystick_horizontal': 0,
            'right_joystick_vertical': 0,
            'arrow_horizontal': 0,
            'arrow_vertical': 0
        }

        # Initialize buttons
        self.buttons = {
            'x': 0,
            'square': 0,
            'circle': 0,
            'triangle': 0,
            'l1': 0,
            'r1': 0
        }

    def update(self):
        pygame.event.pump()
        
        # Update joystick values
        self.axes['left_joystick_horizontal'] = self.round_axis(self.joystick.get_axis(0))
        self.axes['left_joystick_vertical'] = self.round_axis(self.joystick.get_axis(1))
        self.axes['right_joystick_horizontal'] = self.round_axis(self.joystick.get_axis(2))
        self.axes['right_joystick_vertical'] = self.round_axis(self.joystick.get_axis(3))

        # Update arrow keys values
        self.axes['arrow_horizontal'] = self.round_axis(self.joystick.get_hat(0)[0])
        self.axes['arrow_vertical'] = self.round_axis(self.joystick.get_hat(0)[1])

        # Update button values
        self.buttons['x'] = self.joystick.get_button(0)
        self.buttons['circle'] = self.joystick.get_button(1)
        self.buttons['square'] = self.joystick.get_button(2)
        self.buttons['triangle'] = self.joystick.get_button(3)
        self.buttons['l1'] = self.joystick.get_button(4)
        self.buttons['r1'] = self.joystick.get_button(5)

    def round_axis(self, value):
        if abs(value) > 0.2:
            return 1 if value > 0 else -1
        return 0

    def is_button_pressed(self, button):
        return self.buttons.get(button, False)

    def get_axis(self, axis):
        return self.axes.get(axis, 0)

if __name__ == "__main__":
    gc = GameController()
    print("Press any button or move any joystick...")

    while True:
        gc.update()

        # Check all buttons
        for button in ['x', 'circle', 'square', 'triangle', 'l1', 'r1']:
            if gc.is_button_pressed(button):
                print(f"'{button}' button is pressed.")

        # Check all axes
        for axis in ['left_joystick_horizontal', 'left_joystick_vertical', 'right_joystick_horizontal', 'right_joystick_vertical', 'arrow_horizontal', 'arrow_vertical']:
            value = gc.get_axis(axis)
            if value != 0:
                print(f"'{axis}' axis is moved. Value: {value}")

        time.sleep(0.1)  # To prevent the script from running too fast
