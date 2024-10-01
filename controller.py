from motor import Motor
import time
from pynput import keyboard

if __name__ == "__main__":
    
    print("Welcome to the controller...")
    motor_0 = Motor(0)
    motor_1 = Motor(1)
    motor_2 = Motor(2)
    motor_3 = Motor(3)
    motors = [motor_0, motor_1, motor_2, motor_3]
    motor_0.set_rotation(90)
    
    while(True):
        pulse = input("enter angle: ")
        pulse = int(pulse)
        motor_0.set_rotation(pulse)
    
