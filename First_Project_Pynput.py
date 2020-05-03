#Lets go!!

from pynput.mouse import Button, Listener

def click(x,y, button, pressed):
    print(x,y, button, pressed)
    return False

def move(x,y):
    print(x,y)

with Listener(on_click=click, on_move=move) as listener:
    listener.join()