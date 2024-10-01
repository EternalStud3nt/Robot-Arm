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
    motor_0.set_rotation(0)

    motor = Motor(0)

    def on_press(key):
        try:
            if key == keyboard.Key.left:  # Left arrow key
                motor.rotate(-1)
                print("Rotating left")
                time.sleep(0.04)  # Pause to avoid rapid rotation
            elif key == keyboard.Key.right:  # Right arrow key
                motor.rotate(+1)
                print("Rotating right")
                time.sleep(0.04)  # Pause to avoid rapid rotation
        except AttributeError:
            pass

    def on_release(key):
        if key == keyboard.Key.esc:
            # Stop listener on 'esc' press
            return False

    # Start listening for keypresses
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
