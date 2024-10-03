import time
from pynput import keyboard
from event import Event 

rotate_left_event = Event()
rotate_right_event = Event()
rotate_forwards_event = Event()
rotate_upwards_event = Event()

def on_press(key):
    if key == keyboard.Key.left:
        rotate_left_event.invoke(time.time())  # Invoke event with current time
    elif key == keyboard.Key.right:
        rotate_right_event.invoke(time.time())
    elif key == keyboard.Key.up:
        rotate_forwards_event.invoke(time.time())
    elif key == keyboard.Key.down:
        rotate_upwards_event.invoke(time.time())

def on_release(key):
    if key == keyboard.Key.left:
        rotate_left_event.invoke(None)  # Stop rotating left
    elif key == keyboard.Key.right:
        rotate_right_event.invoke(None)  # Stop rotating right
    elif key == keyboard.Key.up:
        rotate_forwards_event.invoke(None)  # Stop rotating forwards
    elif key == keyboard.Key.down:
        rotate_upwards_event.invoke(None)  # Stop rotating upwards

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()