from motor import Motor
from PCA9685 import PCA9685
import time
import keyboard

rotation_speed = 100  # degrees per second
moving_forwards = False
moving_backwards = False
moving_upwards = False
moving_downwards = False
rotating_left = False
rotating_right = False
last_time = time.time()

#region Motor control functions
def move_forwards():
    global moving_forwards
    moving_forwards = True

def stop_forwards():
    global moving_forwards
    moving_forwards = False

def move_backwards():
    global moving_backwards
    moving_backwards = True

def stop_backwards():
    global moving_backwards
    moving_backwards = False

def move_upwards():
    global moving_upwards
    moving_upwards = True

def stop_upwards():
    global moving_upwards
    moving_upwards = False

def move_downwards():
    global moving_downwards
    moving_downwards = True

def stop_downwards():
    global moving_downwards
    moving_downwards = False

def rotate_left():
    global rotating_left
    rotating_left = True

def stop_rotate_left():
    global rotating_left
    rotating_left = False

def rotate_right():
    global rotating_right
    rotating_right = True

def stop_rotate_right():
    global rotating_right
    rotating_right = False
#endregion

# Debug function for manual angle input
def debug_arm():
    while True:
        pulse = input("Enter angle: ")
        pulse = int(pulse)
        motor_0.set_rotation(pulse)

# Handle the input from the keyboard
def handle_input():
    global rotation_speed, moving_forwards, moving_backwards, moving_upwards, moving_downwards, rotating_left, rotating_right, last_time, motor_0, motor_1, motor_2
    try:
        while True:
            current_time = time.time()
            time_delta = current_time - last_time  # Time since last update

            if moving_forwards:
                motor_1.rotate(rotation_speed * time_delta)  # Move forwards
            if moving_backwards:
                motor_1.rotate(-rotation_speed * time_delta)  # Move backwards
            if moving_upwards:
                motor_2.rotate(rotation_speed * time_delta)  # Move upwards
            if moving_downwards:
                motor_2.rotate(-rotation_speed * time_delta)  # Move downwards
            if rotating_left:
                motor_0.rotate(-rotation_speed * time_delta)  # Rotate left
            if rotating_right:
                motor_0.rotate(rotation_speed * time_delta)  # Rotate right
            
            last_time = current_time  # Update the last_time
            time.sleep(0.01)  # Small delay to avoid high CPU usage

    except KeyboardInterrupt:
        print("\nController stopped.")

def initialize():
    global motor_0, motor_1, motor_2

    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)
    keyboard.on_left_arrow_press.subscribe(rotate_left)
    keyboard.on_left_arrow_release.subscribe(stop_rotate_left)
    keyboard.on_right_arrow_press.subscribe(rotate_right)
    keyboard.on_right_arrow_release.subscribe(stop_rotate_right)
    keyboard.on_up_arrow_press.subscribe(move_forwards)
    keyboard.on_up_arrow_release.subscribe(stop_forwards)
    keyboard.on_down_arrow_press.subscribe(move_backwards)
    keyboard.on_down_arrow_release.subscribe(stop_backwards)
    keyboard.on_space_press.subscribe(move_upwards)
    keyboard.on_space_release.subscribe(stop_upwards)
    keyboard.on_shift_press.subscribe(move_downwards)
    keyboard.on_shift_release.subscribe(stop_downwards)
    
    motor_0 = Motor(0, pwm)
    motor_1 = Motor(1, pwm)
    motor_2 = Motor(2, pwm)
    motor_0.set_rotation(90)
    motor_1.set_rotation(90)
    motor_2.set_rotation(90)

if __name__ == "__main__":
    print("Welcome to the controller...")
    initialize()
    handle_input()