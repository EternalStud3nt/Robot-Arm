from motor import Motor
import time
from pynput import keyboard

rotation_speed = 30  # degrees per second

def on_press(key):
    global rotating_left, rotating_right, last_time
    if key == keyboard.Key.left:
        rotating_left = True
        last_time = time.time()  # Record the time when key is pressed
    elif key == keyboard.Key.right:
        rotating_right = True
        last_time = time.time()

def on_release(key):
    global rotating_left, rotating_right
    if key == keyboard.Key.left:
        rotating_left = False
    elif key == keyboard.Key.right:
        rotating_right = False

# Debug function for manual angle input
def manual_control():
    while True:
        pulse = input("Enter angle: ")
        pulse = int(pulse)
        motor_0.set_rotation(pulse)

if __name__ == "__main__":
    
    print("Welcome to the controller...")
    motor_0 = Motor(0)
    motor_0.set_rotation(90)
    
    rotating_left = False
    rotating_right = False
    last_time = time.time()

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    try:
        while True:
            current_time = time.time()
            time_delta = current_time - last_time  # Time since last update

            if rotating_left:
                motor_0.rotate(-rotation_speed * time_delta)  # Rotate left
            elif rotating_right:
                motor_0.rotate(rotation_speed * time_delta)  # Rotate right
            
            last_time = current_time  # Update the last_time
            time.sleep(0.01)  # Small delay to avoid high CPU usage

        # Uncomment the following line to use the debug function:
        # manual_control()

    except KeyboardInterrupt:
        listener.stop()
        print("\nController stopped.")
