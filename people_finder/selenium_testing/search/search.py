import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://103.198.137.87:8000/home/login")
driver.maximize_window()
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
    search_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
    search_btn.click()
except:
    print("Search page couldn't be loaded ❌")

try:
    # assert 'Azim' in driver.page_source, "Search could not find the user (19201026@uap-bd.edu) ❌"
    output_box = driver.find_elements(By.XPATH, './/td')
    datas = [item.text for item in output_box]
    assert "19201026@uap-bd.edu" in datas, 'Test: Search could not find the user (19201026@uap-bd.edu) ❌'
    print("Test: Search found the user (19201026@uap-bd.edu) ✅")
except AssertionError as msg:
    print(msg)
time.sleep(2)
#This case should fail
try:
    search_inp = driver.find_element(By.XPATH, '//*[@id="id_search_text"]')
    search_inp.clear()
    search_inp.send_keys('111111')
    search_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
    search_btn.click()
except Exception as msg:
    print("Search page couldn't be loaded ❌")
    print(msg)
try:
    # assert 'Azim' in driver.page_source, "Search could not find the user (19201026@uap-bd.edu) ❌"
    output_box = driver.find_elements(By.XPATH, './/td')
    datas = [item.text for item in output_box]
    assert "111111@uap-bd.edu" in datas, 'Test: Search could not find the user (111111@uap-bd.edu) ❌'
    print("Test: Search found the user (19201026@uap-bd.edu) ✅")
except AssertionError as msg:
    print(msg)

try:
    search_inp = driver.find_element(By.XPATH, '//*[@id="id_search_text"]')
    search_inp.clear()
    search_inp.send_keys('Busra')
    search_btn = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
    search_btn.click()
except Exception as msg:
    print("Search page couldn't be loaded ❌")
    print(msg)
try:
    # assert 'Azim' in driver.page_source, "Search could not find the user (19201026@uap-bd.edu) ❌"
    output_box = driver.find_elements(By.XPATH, './/td')
    datas = [item.text for item in output_box]
    assert "19201048@uap-bd.edu" in datas, 'Test: Search could not find the user Busra (19201048@uap-bd.edu) ❌'
    print("Test: Search found the user Busra (19201048@uap-bd.edu) ✅")
except AssertionError as msg:
    print(msg)

time.sleep(1)
driver.close()
exit(0)