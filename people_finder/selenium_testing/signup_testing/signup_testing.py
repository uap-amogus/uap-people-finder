import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("http://103.198.137.87:8000/home/signup")
time.sleep(2)

try:
    email_field = driver.find_element(By.XPATH, '//*[@id="id_email"]')
    check_box = driver.find_element(By.XPATH, '//*[@id="id_accept_terms"]')
    check_box.click()
    email_field.clear()
    email_field.send_keys('19201052@uap-bd.edu')
    signup_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
    signup_btn.click()
    time.sleep(1)
    confirm_text = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div')
    assert 'An e-mail was sent to you with the credentials!' in confirm_text.text, "Test: Signup unsuccessful ❌"
    print("Test: Signup successful ✅")
except AssertionError as msg:
    print(msg)
    
#this case should fail
try:
    email_field = driver.find_element(By.XPATH, '//*[@id="id_email"]')
    check_box = driver.find_element(By.XPATH, '//*[@id="id_accept_terms"]')
    check_box.click()
    email_field.clear()
    email_field.send_keys('19201052@uap-bd.edu')
    signup_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
    signup_btn.click()
    time.sleep(1)
    confirm_text = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div')
    assert 'An e-mail was sent to you with the credentials!' in confirm_text.text, "Test: Signup unsuccessful ❌"
    print("Test: Signup successful ✅")
except AssertionError as msg:
    print(msg)
