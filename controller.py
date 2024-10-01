from motor import Motor
import time
import keyboard

if __name__ == "__main__":
    
    print("Welcome to the controller...")
    motor_0 = Motor(0)
    motor_1 = Motor(1)
    motor_2 = Motor(2)
    motor_3 = Motor(3)
    motors = [motor_0, motor_1, motor_2, motor_3]
    
    for motor in motors:
        time.sleep(1)
        motor.set_rotation(90)

    def rotate_motor():
        motor = Motor(0)
        while True:
            
            if keyboard.is_pressed('left'):
                motor.rotate(-1)
                print("Rotating left")
                time.sleep(0.04)
            elif keyboard.is_pressed('right'):
                motor.set_rotation(+1)
                print("Rotating right")
                time.sleep(0.04)

    rotate_motor()