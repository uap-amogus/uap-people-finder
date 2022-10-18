from distutils.log import info
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome() 
driver.get("http://103.198.137.87:8000/home/login")
time.sleep(3)

username_field = driver.find_element(By.XPATH, '//*[@id="id_username"]')
password_field = driver.find_element(By.XPATH, '//*[@id="id_password"]')

username_field.clear()
username_field.send_keys('19201048@uap-bd.edu')
password_field.clear()
password_field.send_keys('SJEx8ttw')

#You are now logged in.
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
login_button.click()
time.sleep(3)


if 'Welcome, 19201048@uap-bd.edu' in driver.page_source:
    print("Logged in")
else:
    print("Not logged in")


try:
    interst1 = driver.find_element(By.XPATH, '//*[@id="id_interest_1"]')
    interst1 = Select(interst1)
    interst1.select_by_value('Photography')
    print("Test: Selection of Interest 1 Successful (Photography) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (Photography) ❌")
 
try:
    interest2 = driver.find_element(By.XPATH, '//*[@id="id_interest_2"]')
    interest2 = Select(interst1)
    interest2.select_by_value('googling')
    print("Test: Selection of Interest 1 Successful (googling) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (googling) ❌")



#interest 2
try:
    interst2 = driver.find_element(By.XPATH, '//*[@id="id_interest_2"]')
    interst2 = Select(interst2)
    interst2.select_by_value('Programming')
    print("Test: Selection of Interest 2 Successful (Programming) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (Programming) ❌")
 
try:
    interest3 = driver.find_element(By.XPATH, '//*[@id="id_interest_3"]')
    interest3 = Select(interst2)
    interest3.select_by_value('facebooking')
    print("Test: Selection of Interest 2 Successful (facebooking) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (facebooking) ❌")



try:
    interst3 = driver.find_element(By.XPATH, '//*[@id="id_interest_3"]')
    interst3 = Select(interst3)
    interst3.select_by_value('Dance')
    print("Test: Selection of Interest 3 Successful (Dance) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (Dance) ❌")
 
try:
    interest2 = driver.find_element(By.XPATH, '//*[@id="id_interest_2"]')
    interest2 = Select(interst3)
    interest2.select_by_value('singing')
    print("Test: Selection of Interest 3 Successful (singing) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (singing) ❌")



save_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
save_button.click()
time.sleep(1.5)


#check data
try:
    interst1 = driver.find_element(By.XPATH, '//*[@id="id_interest_1"]')
    assert interst1.get_attribute('value') == "Photography", "Test: Interest selection does not match (Photography) ❌"
    print("Test: Selection of Interest 1 matches (Photography) ✅")
except AssertionError as msg:
    print(msg)
try:
    interst1 = driver.find_element(By.XPATH, '//*[@id="id_interest_1"]')
    assert interst1.get_attribute('value') == "Programming", "Test: Interest selection does not match (Programming) ❌"
    print("Test: Selection of Interest 1 matches (Programming) ✅")
except AssertionError as msg:
    print(msg)

#interest2
try:
    interst2 = driver.find_element(By.XPATH, '//*[@id="id_interest_2"]')
    assert interst2.get_attribute('value') == "Programming", "Test: Interest selection does not match (Programming) ❌"
    print("Test: Selection of Interest 2 matches (Programming) ✅")
except AssertionError as msg:
    print(msg)
try:
    interst2 = driver.find_element(By.XPATH, '//*[@id="id_interest_2"]')
    assert interst2.get_attribute('value') == "Photography", "Test: Interest selection does not match (Photography) ❌"
    print("Test: Selection of Interest 2 matches (Photography) ✅")
except AssertionError as msg:
    print(msg)

#interest3

try:
    interst3 = driver.find_element(By.XPATH, '//*[@id="id_interest_3"]')
    assert interst3.get_attribute('value') == "Dance", "Test: Interest selection does not match (Dance) ❌"
    print("Test: Selection of Interest 3 matches (Dance) ✅")
except AssertionError as msg:
    print(msg)
try:
    interst3 = driver.find_element(By.XPATH, '//*[@id="id_interest_3"]')
    assert interst3.get_attribute('value') == "Movies", "Test: Interest selection does not match (Movies) ❌"
    print("Test: Selection of Interest 3 matches (Movies) ✅")
except AssertionError as msg:
    print(msg)

#driver.close()