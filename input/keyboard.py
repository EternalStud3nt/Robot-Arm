import time
from pynput import keyboard
from input.event import Event 

on_left_arrow_press = Event()
on_right_arrow_press = Event()
on_up_arrow_press = Event()
on_down_arrow_press = Event()
on_space_press = Event()
on_shift_press = Event()
on_z_press = Event()
on_x_press = Event()

on_left_arrow_release = Event()
on_right_arrow_release = Event()
on_up_arrow_release = Event()
on_down_arrow_release = Event()
on_space_release = Event()
on_shift_release = Event()
on_z_release = Event()
on_x_release = Event()

def on_press(key):
    try:
        if key == keyboard.Key.left:
            on_left_arrow_press.invoke()
        elif key == keyboard.Key.right:
            on_right_arrow_press.invoke()
        elif key == keyboard.Key.up:
            on_up_arrow_press.invoke()
        elif key == keyboard.Key.down:
            on_down_arrow_press.invoke()
        elif key == keyboard.Key.space:
            on_space_press.invoke()
        elif key == keyboard.Key.shift:
            on_shift_press.invoke()
        elif key.char == 'z':
            on_z_press.invoke()
        elif key.char == 'x':
            on_x_press.invoke()
    except:
        pass
def on_release(key):
    try:
        if key == keyboard.Key.left:
            on_left_arrow_release.invoke()
        elif key == keyboard.Key.right:
            on_right_arrow_release.invoke()
        elif key == keyboard.Key.up:
            on_up_arrow_release.invoke()
        elif key == keyboard.Key.down:
            on_down_arrow_release.invoke()
        elif key == keyboard.Key.space:
            on_space_release.invoke()
        elif key == keyboard.Key.shift:
            on_shift_release.invoke()
        elif key.char == 'z':
            on_z_release.invoke()
        elif key.char == 'x':
            on_x_release.invoke()
    except:
        pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()