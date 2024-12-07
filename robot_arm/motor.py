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
        
        total_steps = abs(target_rotation - self.rotation)
        total_time = 2  # Total time in seconds for the entire rotation
        step_time = total_time / total_steps if total_steps != 0 else 0
        
        step = 1 if target_rotation > self.rotation else -1
        for angle in range(self.rotation, target_rotation, step):
            target_pulse = conversions.angle_to_pulse(angle)
            self.pwm.setServoPulse(self.channel, target_pulse)
            self.rotation = angle
            time.sleep(step_time)  # Adjust the sleep time for desired speed
        
        
        self.pwm.setServoPulse(self.channel, target_pulse)
        self.rotation = target_rotation
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

