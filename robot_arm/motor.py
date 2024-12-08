from robot_arm.PCA9685 import PCA9685
import conversions
import time

class Motor:
    def __init__(self, channel, pca):
        self.channel = channel
        self.pwm = pca
        self.initialize_rotation(90)
        self.angular_speed = 67.5 

    def initialize_rotation(self, initial_rotation):
        self.rotation = initial_rotation
        pulse = conversions.angle_to_pulse(self.rotation)
        self.pwm.setServoPulse(self.channel, pulse) # degrees per second
    
    def set_rotation(self, target_rotation):
        if(target_rotation >= 180): target_rotation = 180
        if(target_rotation <= 0): target_rotation = 0
        
        delta_angle = target_rotation - self.rotation
        delta_pulse = conversions.angle_to_pulse(delta_angle)
        initial_pulse = conversions.angle_to_pulse(self.rotation)
        
        for i in range(1, 11):
            new_pulse = initial_pulse + (delta_pulse / 10) * i
            self.pwm.setServoPulse(self.channel, new_pulse)
            time.sleep(0.1)
        
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

