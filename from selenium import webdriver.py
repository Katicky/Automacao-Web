from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
sleep(2)
try:
    usuario = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')
    usuario.send_keys('standard_user')
    
    senha = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
    senha.click()
    senha.send_keys('secret_sauce')
    sleep(2)
    senha.send_keys(Keys.ENTER)
    sleep(2)
    
    add = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    add.click()
    sleep(2)
    
    carrinho = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
    carrinho.click()
    sleep(3)
    
    check = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/button[2]')
    check.click()
    sleep(2)
    
    first = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input')
    first.click()
    first.send_keys('Pedro')
    
    last = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input')
    last.click()
    last.send_keys('Bueno')
    
    postal = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input')
    postal.click()
    postal.send_keys('123456')
    sleep(2)
    
    continuar = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[2]/input')
    continuar.click()
    sleep(2)
    
    finish = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]')
    finish.click()


except NoSuchElementException:
    print('tente novamente')
sleep(2)

puooo= 0
