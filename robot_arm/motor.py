from robot_arm.PCA9685 import PCA9685
import time
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
        
        # Send pulse over 50 steps to simulate smooth movement
        current_pulse = conversions.angle_to_pulse(self.rotation)
        step = (pulse - current_pulse) / 50  # 50 steps for 1 second
        for i in range(50):
            current_pulse += step
            self.pwm.setServoPulse(self.channel, current_pulse)
            time.sleep(0.02)  # 20 ms per step
            
        self.rotation = angle
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

