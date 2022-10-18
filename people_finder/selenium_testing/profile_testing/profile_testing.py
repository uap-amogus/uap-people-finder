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

# SEND & SAVE DATA
#########################################################################################################################

fname = "Islam"
lname = "Azim"
try:
    first_name = driver.find_element(By.XPATH, '//*[@id="id_first_name"]')
    last_name = driver.find_element(By.XPATH, '//*[@id="id_last_name"]')
    first_name.clear()
    last_name.clear()
    first_name.send_keys(fname)
    last_name.send_keys(lname)
    print("Test: Sending keys to First Name & Last Name Successfull ✅")
except:
    print("Test: Sending keys to First Name & Last Name Unsuccessfull ❌")


try:
    interst1 = driver.find_element(By.XPATH, '//*[@id="id_interest_1"]')
    interst1 = Select(interst1)
    interst1.select_by_value('Photography')
    print("Test: Selection of Interest 1 Successful (Photography) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (Photography) ❌")
# this will fail
try:
    interest2 = driver.find_element(By.XPATH, '//*[@id="id_interest_2"]')
    interest2 = Select(interst1)
    interest2.select_by_value('Googling')
    print("Test: Selection of Interest 1 Successful (Googling) ✅")
except Exception as msg:
    print("Test: Interest Selection Failed (Googling) ❌")

try:
    dp_upload = driver.find_element(By.XPATH, '//*[@id="id_display_picture"]')
    dp_upload.send_keys(
        r'E:\prog\uap-people-finder\people_finder\selenium_testing\azim_islam_dp.jpg')
    print("Test: DP uploaded (azim_islam_dp.jpg) ✅")
except:
    print("Test: DP upload failed (azim_islam_dp.jpg) ❌")

save_button = driver.find_element(
    By.XPATH, '/html/body/div/div/div/form/button')
save_button.click()
time.sleep(1.5)


# CHECK DATA
#########################################################################################################################
try:
    first_name = driver.find_element(By.XPATH, '//*[@id="id_first_name"]')
    assert first_name.get_attribute(
        'value') == fname, "Test: First name does not match ❌"
    print("Test: First name matches ✅")
except AssertionError as msg:
    print(msg)
try:
    last_name = driver.find_element(By.XPATH, '//*[@id="id_last_name"]')
    assert last_name.get_attribute(
        'value') == lname, "Test: Last name does not match ❌"
    print("Test: Last name matches ✅")
except AssertionError as msg:
    print(msg)
try:
    last_name = driver.find_element(By.XPATH, '//*[@id="id_last_name"]')
    assert "" == lname, "Test: Null string check pass ❌"
    print("Test: Null string check failed ❌")
except AssertionError as msg:
    print(msg)
try:
    interst1 = driver.find_element(By.XPATH, '//*[@id="id_interest_1"]')
    assert interst1.get_attribute(
        'value') == "Photography", "Test: Interest selection does not match (Photography) ❌"
    print("Test: Selection of Interest 1 matches (Photography) ✅")
except AssertionError as msg:
    print(msg)
# this will fail
try:
    interst1 = driver.find_element(By.XPATH, '//*[@id="id_interest_1"]')
    assert interst1.get_attribute(
        'value') == "Programming", "Test: Interest selection does not match (Programming) ❌"
    print("Test: Selection of Interest 1 matches (Programming) ✅")
except AssertionError as msg:
    print(msg)

try:
    dp = driver.find_element(By.XPATH, '/html/body/div/div/img')
    assert 'azim_islam_dp.jpg' in dp.get_attribute(
        'src'), "Test: Display Picture does not match with (azim_islam_dp.jpg) ❌"
    print("Test: Display Picture matches with (azim_islam_dp.jpg) ✅")
except AssertionError as msg:
    print(msg)
# this will fail
try:
    dp = driver.find_element(By.XPATH, '/html/body/div/div/img')
    assert 'busra_dp.jpg' in dp.get_attribute(
        'src'), "Test: Display Picture does not match with (busra_dp.jpg) ❌"
    print("Test: Display Picture matches with (busra_dp.jpg) ✅")
except AssertionError as msg:
    print(msg)


driver.close()
exit(1)
