#ControllingMouseKeyboardPynput

# Controlling your mouse
# listening to your mouse
# Controlling you keyboard
# listening to your keyboard - Will be finally used in our keylogger

from pynput.mouse import Controller
from pynput.keyboard import Controller

# (left to right, top to buttom)
# From top-left of the screeen you can imagine the top-left to be (0,0)


def controlMouse();
    mouse = Controller()
    mouse.position = (500,200)

def controlKeyboard();
    keyboard = Controller()
    keyboard.type("I am freaking awesome!")

