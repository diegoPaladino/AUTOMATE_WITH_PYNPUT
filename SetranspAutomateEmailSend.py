#SetranspAutomateEmailSend

from selenium import webdriver
from pynput.mouse import Button, Listener, Controller
from pynput.keyboard import Key, Listener
import time

# Openning the page on Opera Navigator
# driver=webdriver.Opera(executable_path='C:\operadriver')
# driver.implicitly_wait(10)
# driver.get('http://www.gemul-aparecida.com.br/login.asp')


#Mouse and Keyboard Actions

mouse=Controller()
keyb=Controller()
# print(mouse.position)
# mouse.position=(1124,109)
# mouse.click(Button.left,1)
# time.sleep(2)
# mouse.position=(699, 406)
# mouse.click(Button.left,1)
# time.sleep(2)
# keyb.type("DIEGO.CSF")
# mouse.position=(699, 467)
# mouse.click(Button.left)
# keyb.type('GMLPALADINO')

keyb.press(Key.cmd)
keyb.release(Key.cmd)
keyb.press('c')
