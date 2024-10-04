from motor import Motor
from PCA9685 import PCA9685
import math


class Robot_Arm:
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
        
        self.reset_motors()
        self.position = [0, 15.5, 8]
        
    def set_rotation(self, motor, angle):
        self.motors[motor].set_rotation(angle)
        
    def set_rotations(self, angles):
        for motor, angle in zip(["base", "depth", "height"], angles):
            self.set_rotation(motor, angle)
        
    def reset_motors(self):
        for motor in self.motors:
            self.motors[motor].set_rotation(90)
            
    def set_position(self, x, y, z):
        if(z < 2.5 or z > 15 or y < 3 or y > 15 or x < 0 or x > 15):
            print("Invalid position")
            return
        
        l_s = 8
        l_xy = math.sqrt(x**2 + y**2)
        l = math.sqrt(l_xy**2 + z**2)
        theta = math.acos((l/2)/l_s)
        phi = math.atan(y/x)
        a1 = phi + theta
        a2 = phi - theta
        
        theta_alpha = a1 - math.pi/2
        theta_beta = -a2
        theta_gamma = phi
        
        self.set_rotations([theta_gamma, theta_alpha, theta_beta])
        self.position = [x, y, z]
        
        