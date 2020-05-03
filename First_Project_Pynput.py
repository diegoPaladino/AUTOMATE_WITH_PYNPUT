#Lets go!!

from pynput.mouse import Button, Listener
from pynput.keyboard import Listener, Key

#Mouse actions

def click(x,y, button, pressed):
    print(x,y, button, pressed)
    return False

def move(x,y):
    print(x,y)

with Listener(on_click=click, on_move=move) as listener:
    listener.join()

#Keyboard actions

def press(key):
    print(key)

def release(key):
    if key == Key.shift:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
