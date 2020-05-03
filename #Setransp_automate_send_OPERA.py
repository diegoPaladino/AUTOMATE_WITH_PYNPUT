#Setransp_automate_send builded with OPERA DRIVER

from selenium import webdriver
from pynput.mouse import Button, Listener
from pynput.keyboard import Listener, Key



driver = webdriver.Opera(executable_path='C:\operadriver')
driver.implicitly_wait(10)

def login():
    #Link: http://www.gemul-aparecida.com.br/login.asp
    id_login='txtLogin'
    id_pass='txtSenha'
    id_btn='#'
    login='DIEGO.CSF'
    passw='GMLPALADINO'
    driver.get('http://www.gemul-aparecida.com.br/login.asp')
    input_login=driver.find_element_by_id(id_login)
    input_pass=driver.find_element_by_id(id_pass)
    btn_login=driver.find_element_by_id(id_btn)
    input_login.send_keys(login)
    input_pass.send_keys(passw)
    btn_login.click()

login()
