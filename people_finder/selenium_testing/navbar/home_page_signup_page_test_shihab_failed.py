from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://103.198.137.87:8000/")
driver.maximize_window()

sleep(2)
signup = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
signup.click()

try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Login', 'Signup page loading failed ❌'
    print("Signup page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
driver.close()
