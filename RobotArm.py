#!/usr/bin/python

from Motor import Motor
from PCA9685 import PCA9685 

class RobotArm:
    
    def __init__(self):
        pwm = PCA9685(0x40, debug=False)
        pwm.setPWMFreq(50)
        
        # Gripper
        self.motor_0 = Motor(pwm, 0, -90, 0, 90, 480, 1500, 2500)
        # Vertical Rotation
        self.motor_1 = Motor(pwm, 1, -90, 0, 90, 512, 1524, 2580)
        # Z Position
        self.motor_2 = Motor(pwm,2, -45, 0, 81, 2000, 1500, 600)
        # Y Position
        self.motor_3 = Motor(pwm, 3, -45, 0, 90, 1000, 1500, 2500)
        
        self.motors = [self.motor_0, self.motor_1, self.motor_2, self.motor_3]
    
    def debug(self):
        
        try:
            while True:
                channel_input = input("Enter channel number (0-15): ")
                pulse_input = input("Enter pulse width (500 - 2500): ")

                channel = int(channel_input)
                pulse = int(pulse_input)
                selected_motor = self.motors[channel]

                if selected_motor != None:
                    selected_motor.send_pulse(pulse)
                    print(f"Set pulse {pulse}us for channel {channel}.")
                else:
                    print("Invalid input. Channel should be between 0 and 15")
        except KeyboardInterrupt:
            print("\nExiting the program.")
    
    def set_position(self, x, y, z):
        pass
