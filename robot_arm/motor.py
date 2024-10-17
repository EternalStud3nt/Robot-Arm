from PCA9685 import PCA9685
import conversions

class Motor:
    def __init__(self, channel, pca):
        self.channel = channel
        self.pwm = pca
        self.rotation = 0
        self.set_rotation(90)
    
    def set_rotation(self, angle):
        if(angle >= 180): angle = 180
        if(angle <= 0): angle = 0
        
        pulse = conversions.angle_to_pulse(angle)
        self.pwm.setServoPulse(self.channel, pulse)
        self.rotation = angle
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

