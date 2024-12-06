from robot_arm.motor import Motor
from robot_arm.PCA9685 import PCA9685
import math
import time


class RobotArm:
    def __init__(self) -> None:
        pwm = PCA9685(0x40, debug=False)
        pwm.setPWMFreq(50)
        
        self.base_motor = Motor(0, pwm) # base motor
        self.depth_motor = Motor(8, pwm) # depth arm motor
        self.height_motor = Motor(4, pwm) # height arm motor
        self.claw_motor = Motor(12, pwm) # claw motor
        
        self.max_d_motor_rotation = 170
        self.max_h_motor_rotation = 110
        self.min_h_motor_rotation = 10
        self.min_d_motor_rotation = 5
        self.min_grip = 15
        
        self.motors = {
            "base": self.base_motor,
            "depth": self.depth_motor,
            "height": self.height_motor,
            "claw": self.claw_motor
        }
        
        self.l1 = 8
        self.rotation = 0
        self.depth = 8
        self.height = 8
        self.grip = 90
        self.reset()
        
    def set_rotation_xz(self, angle):
        new_angle = angle + 90
        
        if not(new_angle >= 0 and new_angle <= 180):
            return
        
        self.base_motor.set_rotation(angle + 90)
        self.rotation = angle
        print(f"Current depth: {self.depth}, height: {self.height}, base rotation: {self.rotation}, grip: {self.grip}")
        
    def rotate_by_xz(self, angle):
        self.set_rotation_xz(self.rotation + angle)
        
    def set_motor_rotation(self, motor_id, angle):
        self.motors[motor_id].set_rotation(angle)
        
    def set_depth(self, depth):
        if(depth > 15 or depth < 4 or self.height > 15 or self.height < -5):
            return
        
        try:
            h = self.height
            d = depth
            
            l = math.sqrt(h**2 + d**2)
            
            # theoritical angles in radians
            theta = math.atan(h/d)
            phi = math.acos((l/2)/self.l1)
            a1 = theta + phi
            a2 = theta - phi
        except:
            print("It's not possible to reach that depth")
            return
        
        theta_depth = math.pi - a1
        theta_height = math.pi/2 + a2
        
        theta_depth_deg = math.degrees(theta_depth)
        theta_height_deg = math.degrees(theta_height)
        
        
        
        if(theta_depth_deg < self.min_d_motor_rotation or theta_depth_deg > self.max_d_motor_rotation):
            print("Impossible to reach that position")
            return
        elif(theta_height_deg < self.min_h_motor_rotation or theta_height_deg > self.max_h_motor_rotation):
            print("Impossible to reach that position")
            return
        
        self.depth_motor.set_rotation(theta_depth_deg)
        self.height_motor.set_rotation(theta_height_deg)
        
        
        self.depth = depth
        print(f"Current depth: {self.depth}, height: {self.height}, base rotation: {self.rotation}, grip: {self.grip}")

    def move_forwards(self, distance):
        self.set_depth(self.depth + distance)
        
    def set_height(self, height):
        if(self.depth > 15 or self.depth < 4 or height > 15 or height < -5):
            return
        
        try:
            h = height
            d = self.depth
            
            l = math.sqrt(h**2 + d**2)
            
            # theoritical angles in radians
            theta = math.atan(h/d)
            phi = math.acos((l/2)/self.l1)
            a1 = theta + phi
            a2 = theta - phi
        except:
            print("It's not possible to reach that height")
            return
        
        theta_depth = math.pi - a1
        theta_height = math.pi/2 + a2
        
        theta_depth_deg = math.degrees(theta_depth)
        theta_height_deg = math.degrees(theta_height)
        
        
        
        if(theta_depth_deg < self.min_d_motor_rotation or theta_depth_deg > self.max_d_motor_rotation):
            print("Impossible to reach that position")
            return
        elif(theta_height_deg < self.min_h_motor_rotation or theta_height_deg > self.max_h_motor_rotation):
            print("Impossible to reach that position")
            return
        
        self.depth_motor.set_rotation(theta_depth_deg)
        self.height_motor.set_rotation(theta_height_deg)
        
        self.height = height
        print(f"Current depth: {self.depth}, height: {self.height}, base rotation: {self.rotation}, grip: {self.grip}")

    def move_upwards(self, distance):
        self.set_height(self.height + distance)

    def get_position(self):
        x = self.depth * math.sin(math.radians(self.rotation))
        z = self.depth * math.cos(math.radians(self.rotation))
        y = self.height
        return (x, y, z)
    
    def set_position(self, x, y, z):
        depth = math.sqrt(x**2 + z**2)
        rotation = math.degrees(math.atan2(x, z))
        
        self.set_rotation_xz(rotation)
        self.set_depth(depth)
        self.set_height(y)
        
    def set_grip(self, grip):
        if grip < self.min_grip: grip = self.min_grip
        elif grip > 90: grip = 90
        
        angle = grip * 180 / 100
        self.claw_motor.set_rotation(angle)
        self.grip = grip
        print(grip)
        
    def change_grip(self, delta_grip):
        self.set_grip(self.grip + delta_grip)
               
    def reset(self):
        self.set_grip(90)
        time.sleep(0.2)
        self.set_height(8)
        time.sleep(0.2)
        self.set_depth(8)
        
if __name__ == "__main__":
    arm = RobotArm()
    arm.reset()
    while True:
        motor_channel = input("Enter motor channel (base, depth, height, claw): ").strip().lower()
        if motor_channel not in arm.motors:
            print("Invalid motor channel. Please try again.")
            continue
        
        try:
            degrees = float(input("Enter degrees to rotate: "))
        except ValueError:
            print("Invalid input for degrees. Please enter a number.")
            continue
        
        arm.set_motor_rotation(motor_channel, degrees)
        
        