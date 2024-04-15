#!/usr/bin/python

from PCA9685 import PCA9685 

class Motor:
    last_rotation = 90
    
    def __init__(self,pwm, channel, min_angle, zero_angle, max_angle, min_pulse, zero_pulse, max_pulse):
        self.pwm = pwm
        self.channel = channel
        self.min_angle = min_angle
        self.zero_angle = zero_angle
        self.max_angle = max_angle
        self.min_pulse = min_pulse
        self.zero_pulse = zero_pulse
        self.max_pulse = max_pulse
    
    def get_pulse_from_angle(self, angle):
        if(angle == self.min_angle): return self.min_pulse
        if(angle == self.zero_angle): return self.zero_pulse
        if(angle == self.max_angle): return self.max_pulse
        
        if(angle >= self.min_angle and angle <= self.max_angle):
            pulse_per_angle = 2000 / 180
            output_pulse = pulse_per_angle * angle + 1512
            return output_pulse   
        
        else:
            raise ValueError("This motor (" + str(self.channel) + ") does not support the requested rotation angle: " + str(angle))
            
    
    def set_rotation(self, angle):
        pulse = self.get_pulse_from_angle(angle)
        self.send_pulse(pulse)
        self.last_rotation = angle
    
    def send_pulse(self, pulse):
        if(pulse >= self.min_pulse and pulse <= self.max_pulse):
            self.pwm.setServoPulse(self.channel, pulse)
        else:
            raise ValueError("The pulse you are trying to send in channel: " + str(self.channel) + " is not supported by design. " + str(pulse))
