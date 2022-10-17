from distutils.log import info
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By


driver = webdriver.Chrome() 
driver.get("http://103.198.137.87:8000/home/login")
time.sleep(2)

username_field = driver.find_element(By.XPATH, '//*[@id="id_username"]')
password_field = driver.find_element(By.XPATH, '//*[@id="id_password"]')

username_field.send_keys('19201026@uap-bd.edu')
password_field.send_keys('@abcd1234')



login_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
login_button.click()
time.sleep(2)

if 'Welcome, 19201026@uap-bd.edu' in driver.page_source:
    print("Logged in")
else:
    print("Not logged in")