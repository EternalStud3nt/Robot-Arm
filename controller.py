from input_manager import InputManager
import time
from robot_arm import RobotArm

class Controller:
    def __init__(self):
        self.move_speed = 8  # centimeters per second
        self.rotation_speed = 100 # degrees per second
        self.last_time = time.time()
        
        print("Welcome to the controller...")
        self.input_manager = InputManager()
        self.robot = RobotArm()
        self.handle_input()

    # Debug function for ma  nua           l angle input
    def debug_arm(self):
        while True:
            pulse = input("Enter angle: ")
            pulse = int(pulse)
            self.motor_2.set_rotation(pulse)

    # Handle the input from the keyboard
    def handle_input(self):
        try:
            while True:
                current_time = time.time()
                delta_time = current_time - self.last_time  # Time since last update
                input = self.input_manager.arrow_input
                input_x = input[0]
                input_y = input[1]
                
                if(input_x != 0):
                    val = input_x * self.rotation_speed * delta_time
                    self.robot.rotate_by(val)
                if self.input_manager.space_pressed:
                    self.robot.move_upwards(self.move_speed * delta_time)
                elif self.input_manager.shift_pressed:
                    self.robot.move_upwards(- self.move_speed * delta_time)
                if(input_y != 0):
                    self.robot.move_forwards(input_y * self.move_speed * delta_time)
                
                
                
                
                time.sleep(0.01)  # Small delay to avoid h    igh CPU usage
                self.last_time = current_time  # Update the last_time

        except KeyboardInterrupt:
            print("\nController stopped.")

if __name__ == "__main__":                                             
    controller = Controller()  