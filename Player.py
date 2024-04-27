from RobotArm import RobotArm
import Constants

class Player:
    def __init__(self, input_system):
        self.delta_pos_per_second = 1
        self.delta_grip_per_second = 20
        self.robot_arm = RobotArm()
        self.input_system = input_system
        self.register_to_input_actions()
        self.action_to_value = {
            "move_upwards" : [0, 1, 0],
            "move_downwards" : [0, -1, 0],
            "move_left" : [-1, 0, 0],
            "move_right" : [1, 0, 0],
            "move_forwards" : [0, 0, 1],
            "move_backwards" : [0, 0, -1],
            "open_grip" : 1,
            "close_grip" : -1,   
        }
        

    def register_to_input_actions(self):
        for action in self.input_system.action_map.keys():
            # Create a new function that calls handle_action with the action
            handler = lambda action=action: self.handle_input_action(action)
            self.input_system.action_triggered_event.subscribe(handler)

    def handle_input_action(self, action):
        if action.startswith("move"):
            direction = self.action_to_value[action]
            # Multiply each element in the direction list
            direction = [d * Constants.deltatime * self.delta_pos_per_second for d in direction]
            self.robot_arm.change_position(direction)
        if "grip" in action:
            delta_grip = self.action_to_value[action]
            self.robot_arm.change_grip(delta_grip * Constants.deltatime * self.delta_grip_per_second)
