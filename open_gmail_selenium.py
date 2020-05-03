#open the gmail with selenium:

from selenium import webdriver

driver=webdriver.Opera(executable_path='C:\operadriver')
driver.implicitly_wait(10)

def login()
    id_login='identifierId'
    # id_pass=''
    # id_btn=''
    login='diegopaladinoemfrc@gmail.com'
    # passw=''
    driver.get('https://accounts.google.com/signin/v2/identifier?hl=pt-BR&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fclient%3Dopera%26q%3Dgmail%2Blogin%26sourceid%3Dopera%26ie%3DUTF-8%26oe%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    input_login=driver.find_element_by_id(id_login)
    # input_pass=driver.find_element_by_id(id_pass)
    # btn_login=driver.find_element_by_id(id_btn)
    input_login.send_keys(login)
    # input_pass.send_keys(passw)
    # btn_login.click()

login()