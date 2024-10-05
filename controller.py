from input_manager import InputManager
import time
from robot_arm import Robot_Arm

class Controller:
    def __init__(self):
        self.move_speed = 5  # centimeters per second
        self.last_time = time.time()
        
        print("Welcome to the controller...")
        self.input_manager = InputManager()
        self.robot = Robot_Arm()
        self.handle_input()

    # Debug function for manual angle input
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
                
                self.robot.move_sideways(input[0] * self.move_speed * delta_time)
                if self.input_manager.space_pressed:
                    self.robot.move_upwards(self.move_speed * delta_time)
                elif self.input_manager.shift_pressed:
                    self.robot.move_downwards(self.move_speed * delta_time)
                self.robot.move_forwards(input[2] * self.move_speed * delta_time)
                
                self.last_time = current_time  # Update the last_time
                time.sleep(0.01)  # Small delay to avoid high CPU usage

        except KeyboardInterrupt:
            print("\nController stopped.")

if __name__ == "__main__":
    controller = Controller()