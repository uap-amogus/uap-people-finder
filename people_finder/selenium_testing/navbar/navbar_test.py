from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://103.198.137.87:8000/")
driver.maximize_window()

sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[1]/a')
login.click()

#login page loaded successfully
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Login', 'Test: Login page did not load successfully ❌'
    print("Test: Login page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)

signup = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
signup.click()

#login page did not load successfully
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Login', 'Test: Login page did not load successfully ❌'
    print("Test: Login page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[1]/a')
login.click()

#signup page did not load successfully
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Signup', 'Test: Signup page did not load successfully ❌'
    print("Test: Signup page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
signup = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
signup.click()

#signup page loaded successfully
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Signup', 'Test: Signup page did not load successfully ❌'
    print("Test: Signup page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

#login
driver.get("http://103.198.137.87:8000/")

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
    print('Test: Login Successful✅')
except:
    print('Test: Login Failed ❌')

sleep(2)
profile = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
profile.click()

#profile page loaded successfully
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Profile', 'Test: Profile page did not load successfully ❌'
    print("Test: Profile page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[3]/a')
search.click()

#profile page did not load successfully
try:
    assert driver.find_element(By.TAG_NAME,'h2').text == 'Profile', 'Test: Profile page did not load successfully ❌'
    print("Test: Profile page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[3]/a')
search.click()

#search page loaded successfully
try:
    assert driver.find_element(By.TAG_NAME,'h2').text == 'Search', 'Test: Search page did not loaded successfully ❌'
    print("Test: Search page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
profile = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
profile.click()

#search page did not loaded successfully
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Search', 'Test: Search page did not loaded successfully ❌'
    print("Test: Search page loaded successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
profile = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
profile.click()

#logout failed
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Login', 'Test: Logout failed ❌'
    print("Test: Logout successfully ✅") 
except AssertionError as errMsg:
    print(errMsg)

sleep(2)
logout = driver.find_element(By.XPATH, '//*[@id="navbarText"]/ul/li[1]/a')
logout.click()

#logout successful
try:
    assert driver.find_element(By.TAG_NAME,'h1').text == 'Login', 'Test: Logout failed ❌'
    print("Test: Logout successful ✅") 
except AssertionError as errMsg:
    print(errMsg)
sleep(2)

# driver.close()
