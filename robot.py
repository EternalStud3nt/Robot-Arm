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
            print(motor+"-----"+str(angle))
        
    def reset_motors(self):
        for motor in self.motors:
            self.motors[motor].set_rotation(90)
            
    def set_position(self, x, y, z):
        y -= 7.5 # offset due to base height
        if(z < 2.5 or z > 15 or y < -7 or y > 25 or x < 0 or x > 15):
            print("Invalid position")
            return
        
        l_s = 8
        l_xz = math.sqrt(x**2 + z**2)
        l = math.sqrt(l_xz**2 + y**2)
        
        theta = math.acos((l/2)/l_s)
        sigma = math.atan(y/l_xz)
        phi = 0
        if x != 0:
            phi = math.atan(x/z)
        a1 = sigma + theta
        a2 = sigma - theta
        
        theta_alpha = math.pi - a1
        theta_beta = math.pi/2 + a2
        theta_gamma = phi + math.pi/2
        
        theta_alpha = math.degrees(theta_alpha)
        theta_beta = math.degrees(theta_beta)
        theta_gamma = math.degrees(theta_gamma)
        
        self.set_rotations([theta_gamma, theta_alpha, theta_beta])
        self.position = [x, y + 7.5, z]
        
        