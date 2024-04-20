import time
from Event import Event
import KeyboardController as kc
import GameController as gc
from UpdatableType import UpdatableType

class InputSystem(metaclass=UpdatableType):
    def __init__(self):
        self.keyboard_controller = kc.KeyboardController()
        self.game_controller = gc.GameController()

        # Define the action map
        self.action_map = {
            'move_forward': ('up', 'left_joystick_vertical'),
            'move_backward': ('down', 'left_joystick_vertical'),
            'move_left': ('left', 'left_joystick_horizontal'),
            'move_right': ('right', 'left_joystick_horizontal'),
            'move_upwards': ('space', 'x'),
            'move_downwards': ('shift', 'triangle'),
            'open_grip' : ("f", "l1"),
            'close_grip' : ("j", "r1")
            # Add more actions here...
        }

        # Create an event for action triggered
        self.action_triggered_event = Event()

    def is_action_triggered(self, action):
        key, button = self.action_map.get(action, (None, None))
        if key and self.keyboard_controller.is_key_pressed(key):
            return True
        if button:
            if button in self.game_controller.buttons and self.game_controller.is_button_pressed(button):
                return True
            elif button in self.game_controller.axes:
                axis_value = self.game_controller.get_axis(button)
                if action in ['move_forward', 'move_left'] and axis_value < 0:
                    return True
                elif action in ['move_backward', 'move_right'] and axis_value > 0:
                    return True
        return False

    def update(self):
        self.game_controller.update()
        # Check all actions
        for action in self.action_map.keys():
            if self.is_action_triggered(action):
                print(f"Action '{action}' is triggered.")
                # Invoke the event
                self.action_triggered_event.invoke(action)
    
if __name__ == "__main__":
    input_system = InputSystem()
    print("Press any key or button...")
    
    # while True:
    #     input_system.update()