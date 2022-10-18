from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://103.198.137.87:8000/")
driver.maximize_window()

login_email = driver.find_element(By.XPATH, '//*[@id="id_username"]')
login_password = driver.find_element(By.XPATH, '//*[@id="id_password"]')

login_email.clear()
login_password.clear()
sleep(1)
email = "19201051@uap-bd.edu"
password = "shihab@789"

login_email.send_keys(email)
sleep(1)
login_password.send_keys(password)
sleep(1)
login_password.send_keys(Keys.RETURN)
sleep(1)

try:
    profile_link = driver.find_element(By.LINK_TEXT,"Wanna change password? 💀")
    print('Login Successful✅')
except:
    print('Login Failed ❌')

sleep(2)
profile = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
profile.click()

try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Search', 'Search page loading failed ❌'
    print("Search page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
driver.close()
