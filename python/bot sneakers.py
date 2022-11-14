from email import header
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import requests
from selenium import webdriver
import random

proxy_ip_port = "51.103.27.73:8000"
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port
capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)



try :
    driver = webdriver.Firefox(executable_path='driver/geckodriver.exe', desired_capabilities=capabilities)
    driver.get('https://www.nike.com/fr/launch/t/womens-air-jordan-1-starfish')
except:
    print("Can't connect the site")
    pass

def cookie():
    time.sleep(random.randint(1, 5))
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div[2]/button').click()

cookie()

def select_size():
    time.sleep(random.randint(1, 5))

    driver.execute_script('window.scrollTo(0, 750)')
    

    size = 0
    # size 35.5:   /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[1]/button
    # size 36:     /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[2]/button
    # size 36.5:   /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[3]/button
    # size 37.5:   /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[4]/button
    # size 38:     /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[5]/button
    # size 38.5:   /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[6]/button
    # size 39:     /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[7]/button
    # size 40:     /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[8]/button
    # size 40.5 :  /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[9]/button
    # size 41:    /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[10]/button
    # size 42:    /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[11]/button
    # size 42.5:  /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[12]/button
    # size 43:    /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[13]/button
    # size 44:    /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[14]/button
    # size 44.5:  /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[15]/button
    # size 45:    /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[16]/button
    # size 45.5:  /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[17]/button
    # size 46 :   /html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[18]/button
    for size in range(18):
        pass


    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[3]/button').click()
    time.sleep(random.randint(1, 5))
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button').click()
    time.sleep(random.randint(1, 5))
    #driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/div/ul/li[1]/button').click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button').click()

    # //*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[7]/button 39
    # //*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[7]/button
    # //*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[7]
select_size()