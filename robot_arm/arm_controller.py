from input.input_manager import InputManager
import time      
from robot_arm.robot_arm import RobotArm 
        
class ArmController:
    def __init__(self):
        self.move_speed = 6  # centimeters per second
        self.grip_speed = 40  # degrees per second
        self.rotation_speed = 100 # degrees per second         
        self.last_time = time.time()
        
        print("Welcome to the controller...")
        self.input_manager = InputManager()
        self.robot = RobotArm()
        self.handle_input()   

    def debug_arm(self, robot):
        while True:
            pulse = input("Enter angle: ")
            pulse = int(pulse)

    # Handle the input from the keyboard
    def handle_input(self):
        try:
            while True:
                current_time = time.time()
                delta_time = current_time - self.last_time  # Time since last update
                input = self.input_manager.arrow_input
                input_x = input[0]
                input_y = input[1]
                
                # Rotate the robot
                if(input_x != 0):
                    val = input_x * self.rotation_speed * delta_time
                    self.robot.rotate_vertically(val)
                    
                # Move the robot up or down
                if self.input_manager.space_pressed:
                    self.robot.move_upwards(self.move_speed * delta_time)
                elif self.input_manager.shift_pressed:
                    self.robot.move_upwards(- self.move_speed * delta_time)
                    
                # Move the robot forwards or backwards
                if(input_y != 0):
                    self.robot.move_forwards(input_y * self.move_speed * delta_time)
                    
                if(self.input_manager.z_pressed):
                    self.robot.change_grip(self.grip_speed * delta_time)
                elif(self.input_manager.x_pressed):
                    self.robot.change_grip(-self.grip_speed * delta_time)
                
                
                time.sleep(0.005)  # Small delay to avoid h    igh CPU usage
                self.last_time = current_time  # Update the last_time

        except KeyboardInterrupt:
            print("\nController stopped.")
                                            
if __name__ == "__main__":
    controller = ArmController()
#      robot.reset()
#     while True:
#         channel = input("input channel:  ")
#         angle = input("input angle: ")
#         angle = int(angle)
#         robot.set_motor_rotation(channel, angle)
                               