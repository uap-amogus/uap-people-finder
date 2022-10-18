import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("http://103.198.137.87:8000/home/login")
time.sleep(2)

username_field = driver.find_element(By.XPATH, '//*[@id="id_username"]')
password_field = driver.find_element(By.XPATH, '//*[@id="id_password"]')

username_field.send_keys('19201026@uap-bd.edu')
password_field.send_keys('@abcd1234')
login_button = driver.find_element(
    By.XPATH, '/html/body/div/div/div/form/button')
login_button.click()
time.sleep(1)
try:
    assert 'Welcome, 19201026@uap-bd.edu' in driver.page_source
    print("Test: Login successful ✅")
except AssertionError as msg:
    print("Test: Login unsuccessful ❌")

try:
    nav_search_btn = driver.find_element(By.XPATH, '/html/body/div/nav/div/ul/li[3]/a')
    nav_search_btn.click()
    search_text = driver.find_element(By.XPATH, '/html/body/div/div/div/h2')
    print("Search page loaded successfully ✅")
except:
    print("Search page couldn't be loaded successfully ❌")


try:
    search_inp = driver.find_element(By.XPATH, '//*[@id="id_search_text"]')
    search_inp.clear()
    search_text = driver.find_element(By.XPATH, '/html/body/div/div/div/h2')
    print("Search page loaded successfully ✅")
except:
    print("Search page couldn't be loaded ❌")

try:
    search_inp = driver.find_element(By.XPATH, '//*[@id="id_search_text"]')
    search_inp.clear()
    search_inp.send_keys('19201026')
except:
    print("Search page couldn't be loaded ❌")

try:
    assert '19201026@uap-bd.edu' in driver.page_source, "Search could not find the user (19201026@uap-bd.edu) ❌"
    print("Search found the user (19201026@uap-bd.edu) ✅")
except AssertionError as msg:
    print(msg)

#This case should fail
try:
    search_inp = driver.find_element(By.XPATH, '//*[@id="id_search_text"]')
    search_inp.clear()
    search_inp.send_keys('111111')
except:
    print("Search page couldn't be loaded ❌")

try:
    assert '111111@uap-bd.edu' in driver.page_source, "Search could not find the user (111111@uap-bd.edu) ❌"
    print("Search found the user (111111@uap-bd.edu) ✅")
except AssertionError as msg:
    print(msg)