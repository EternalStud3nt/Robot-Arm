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

def move_forwards(event_time):
    global moving_forwards, last_time
    if event_time is not None:
        moving_forwards = True
        last_time = event_time
    else:
        moving_forwards = False

def move_backwards(event_time):
    global moving_backwards, last_time
    if event_time is not None:
        moving_backwards = True
        last_time = event_time
    else:
        moving_backwards = False

def move_upwards(event_time):
    global moving_upwards, last_time
    if event_time is not None:
        moving_upwards = True
        last_time = event_time
    else:
        moving_upwards = False

def move_downwards(event_time):
    global moving_downwards, last_time
    if event_time is not None:
        moving_downwards = True
        last_time = event_time
    else:
        moving_downwards = False

def rotate_left(event_time):
    global rotating_left, last_time
    if event_time is not None:
        rotating_left = True
        last_time = event_time
    else:
        rotating_left = False

def rotate_right(event_time):
    global rotating_right, last_time
    if event_time is not None:
        rotating_right = True
        last_time = event_time
    else:
        rotating_right = False

# Debug function for manual angle input
def control_manually():
    while True:
        pulse = input("Enter angle: ")
        pulse = int(pulse)
        motor_0.set_rotation(pulse)

if __name__ == "__main__":
    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)
    
    print("Welcome to the controller...")
    keyboard.rotate_left_event.subscribe(rotate_left)
    keyboard.rotate_right_event.subscribe(rotate_right)
    keyboard.rotate_forwards_event.subscribe(move_forwards)
    keyboard.rotate_backwards_event.subscribe(move_backwards)
    keyboard.move_upwards_event.subscribe(move_upwards)
    keyboard.move_downwards_event.subscribe(move_downwards)
    
    motor_0 = Motor(0, pwm)
    #manual_control()
    
    motor_1 = Motor(1, pwm)
    motor_2 = Motor(2, pwm)
    motor_0.set_rotation(90)
    motor_1.set_rotation(90)
    motor_2.set_rotation(90)

    try:
        while True:
            current_time = time.time()
            time_delta = current_time - last_time  # Time since last update

            if moving_forwards and not moving_backwards:
                motor_1.rotate(rotation_speed * time_delta)  # Move forwards
            if moving_backwards and not moving_forwards:
                motor_1.rotate(-rotation_speed * time_delta)  # Move backwards
            if moving_upwards and not moving_downwards:
                motor_2.rotate(rotation_speed * time_delta)  # Move upwards
            if moving_downwards and not moving_upwards:
                motor_2.rotate(-rotation_speed * time_delta)  # Move downwards
            if rotating_left and not rotating_right:
                motor_0.rotate(-rotation_speed * time_delta)  # Rotate left
            if rotating_right and not rotating_left:
                motor_0.rotate(rotation_speed * time_delta)  # Rotate right
            
            last_time = current_time  # Update the last_time
            time.sleep(0.01)  # Small delay to avoid high CPU usage

        # Uncomment the following line to use the debug function:
        # manual_control()

    except KeyboardInterrupt:
        print("\nController stopped.")