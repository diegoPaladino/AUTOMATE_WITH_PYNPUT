#SetranspAutomateEmailSend
#tutoriais:
#https://www.youtube.com/watch?v=DTnz8wA6wpw    Simulate Key Presses in Python
#https://www.youtube.com/watch?v=eK7p1e8-6jU    Pynput parte 1 - Controlando o mouse com python
#https://www.youtube.com/watch?v=MYQnqyVqCDc    Pynput parte 2 - Controlando o teclado com python
#https://www.youtube.com/watch?v=2BXr9U6ZL8Y    Simulate Mouse Events in Python
#https://www.youtube.com/watch?v=DTnz8wA6wpw    Simulate Key Presses in Python



from selenium import webdriver
from pynput.mouse import Button, Listener, Controller
from pynput.keyboard import Key, Listener, Controller
import time

# Openning the page on Opera Navigator
# driver=webdriver.Opera(executable_path='C:\operadriver')
# driver.implicitly_wait(10)
# driver.get('http://www.gemul-aparecida.com.br/login.asp')


#Mouse and Keyboard Actions

mouse=Controller()
keyboard=Controller()
print(mouse.position)
# mouse.position=(1124,109)
# mouse.click(Button.left)
# #time.sleep(2)
# mouse.move(699, 406)
# mouse.click(Button.left)
# #time.sleep(2)
# keyboard.type('DIEGO.CSF')
# mouse.move(699, 467)
# mouse.click(Button.left)
# keyb.type('GMLPALADINO')

# keyb.press(Key.cmd)
# keyb.release(Key.cmd)
# keyb.press('c')
