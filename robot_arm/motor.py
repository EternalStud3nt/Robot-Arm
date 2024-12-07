from robot_arm.PCA9685 import PCA9685
import conversions
import time

class Motor:
    def __init__(self, channel, pca):
        self.channel = channel
        self.pwm = pca
        self.rotation = 0
        self.set_rotation(90)
    
    def set_rotation(self, target_rotation):
        if(target_rotation >= 180): target_rotation = 180
        if(target_rotation <= 0): target_rotation = 0
        
        diff = target_rotation - self.rotation
        
        new_rotation = self.rotation + diff/2
        pulse = conversions.angle_to_pulse(new_rotation)
        self.pwm.setServoPulse(self.channel, pulse)
        self.rotation = new_rotation
        time.sleep(0.2)
        
        new_rotation = target_rotation
        pulse = conversions.angle_to_pulse(new_rotation)
        self.pwm.setServoPulse(self.channel, pulse)
        self.rotation = new_rotation
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

