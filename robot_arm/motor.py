from robot_arm.PCA9685 import PCA9685
import conversions
import time

class Motor:
    def __init__(self, channel, pca):
        self.channel = channel
        self.pwm = pca
        self.rotation = 90
        self.angular_speed = 50
        self.set_rotation(90)
        

    def initialize_rotation(self, initial_rotation):
        self.rotation = initial_rotation
        pulse = conversions.angle_to_pulse(self.rotation)
        self.pwm.setServoPulse(self.channel, pulse) # degrees per second
    
    def set_rotation_smooth(self, target_rotation):
        if(target_rotation >= 180): target_rotation = 180
        if(target_rotation <= 0): target_rotation = 0
        
        delta_time = 0.02
        delta_step = self.angular_speed * delta_time
        if(target_rotation < self.rotation): delta_step  *= -1
        number_of_steps = abs(int((target_rotation - self.rotation) / delta_step))
        print(f"Number of steps: {number_of_steps}, Target rotation: {target_rotation}")
        
        for i in range(number_of_steps):
            self.set_rotation(self.rotation + delta_step )
            time.sleep(delta_time)
            
        self.set_rotation(target_rotation)
            
    def set_rotation(self, target_rotation):
        if(target_rotation >= 180): target_rotation = 180
        if(target_rotation <= 0): target_rotation = 0
        
        pulse = conversions.angle_to_pulse(target_rotation)
        self.pwm.setServoPulse(self.channel, pulse)
        self.rotation = target_rotation
        
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation_smooth(new_angle)

