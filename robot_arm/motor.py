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
        
        current_pulse = conversions.angle_to_pulse(self.rotation)
        target_pulse = conversions.angle_to_pulse(target_rotation)
        
        print(f"Current pulse: {current_pulse}, target pulse: {target_pulse}, target rotation: {target_rotation}")
        
        step_count = 50
        step_delay = 1.0 / step_count
        step_size = (target_pulse - current_pulse) / step_count
        
        for step in range(step_count):
            current_pulse += step_size
            self.pwm.setServoPulse(self.channel, current_pulse)
            time.sleep(step_delay)
        
        self.pwm.setServoPulse(self.channel, target_pulse)
        self.rotation = target_rotation
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

