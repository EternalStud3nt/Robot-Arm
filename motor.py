from PCA9685 import PCA9685
import conversions

class Motor:
    def __init__(self, channel):
        self.pwm = PCA9685()
    
    def set_rotation(self, angle):
        pulse = conversions.angle_to_pulse(angle)
        self.pwm.setServoPulse(pulse)
        print("Sending a pulse of: " + pulse)
