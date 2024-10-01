from PCA9685 import PCA9685
import conversions

class Motor:
    def __init__(self, channel):
        self.channel = channel
        self.pwm = PCA9685()
        self.rotation = 0
        self.set_rotation(90)
    
    def set_rotation(self, angle):
        pulse = conversions.angle_to_pulse(angle)
        self.pwm.setServoPulse(self.channel, pulse)
        self.rotation = angle
        print("Sending a pulse of: " + str(pulse))  # Convert pulse to string
    
    def rotate(self, delta_angle):
        new_angle = self.rotation + delta_angle
        self.set_rotation(new_angle)

