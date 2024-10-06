from motor import Motor
from PCA9685 import PCA9685
import math


class RobotArm:
    def __init__(self) -> None:
        pwm = PCA9685(0x40, debug=False)
        pwm.setPWMFreq(50)
        
        self.base_motor = Motor(0, pwm) # base motor
        self.depth_motor = Motor(1, pwm) # depth arm motor
        self.height_motor = Motor(2, pwm) # height arm motor
        self.claw_motor = Motor(3, pwm) # claw motor
        
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
        self.reset()
        
    def set_rotation(self, angle):
        self.base_motor.set_rotation(angle + 90)
        self.rotation = angle
        
    def rotate_by(self, angle):
        self.set_rotation(self.rotation + angle)
        
    def set_depth(self, depth):
        try:
            h = self.height
            d = depth
            
            l = math.sqrt(h**2 + d**2)
            
            # theoritical angles in radians
            theta = math.atan(h/d)
            phi = math.acos((l/2)/self.l1)
            a1 = theta + phi
            a2 = theta - phi
        except ZeroDivisionError:
            print("It's not possible to reach that depth")
            return
        
        theta_depth = math.pi - a1
        theta_height = math.pi/2 + a2
        
        self.depth_motor.set_rotation(math.degrees(theta_depth))
        self.height_motor.set_rotation(math.degrees(theta_height))
        self.depth = depth

    def move_forwards(self, distance):
        self.set_depth(self.depth + distance)
        
    def set_height(self, height):
        try:
            h = height
            d = self.depth
            
            l = math.sqrt(h**2 + d**2)
            
            # theoritical angles in radians
            theta = math.atan(h/d)
            phi = math.acos((l/2)/self.l1)
            a1 = theta + phi
            a2 = theta - phi
        except ZeroDivisionError:
            print("It's not possible to reach that height")
            return
        
        theta_depth = math.pi - a1
        theta_height = math.pi/2 + a2
        
        self.depth_motor.set_rotation(math.degrees(theta_depth))
        self.height_motor.set_rotation(math.degrees(theta_height))
        self.height = height

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
        
        self.set_rotation(rotation)
        self.set_depth(depth)
        self.set_height(y)
               
    def reset(self):
        self.set_rotation(0)
        self.set_depth(8)
        self.set_height(8)
        
        