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

username_field.clear()
username_field.send_keys('19201048@uap-bd.edu')
password_field.clear()
password_field.send_keys('SJEx8ttw')

#You are now logged in.
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
login_button.click()
time.sleep(2)


if 'Welcome, 19201048@uap-bd.edu' in driver.page_source:
    print("Logged in")
else:
    print("Not logged in")


firstname_field = driver.find_element(By.XPATH, '//*[@id="id_first_name"]')
firstname_field.clear()
firstname_field.send_keys('Busra Jahan')

lastname_field = driver.find_element(By.XPATH, '//*[@id="id_last_name"]')
lastname_field.clear()
lastname_field.send_keys('Tanu')

#bio1
interest1_bio_field = driver.find_element(By.XPATH, '//*[@id="id_interest_1_bio"]')
interest1_bio_field.clear()
interest1_bio_field.send_keys('i am a programmer')
#link 1
interest1_link = driver.find_element(By.XPATH, '//*[@id="id_interest_1_link"]')
interest1_link.clear()
interest1_link.send_keys('https://github.com/csbusra')


#bio2
interest2_bio_field = driver.find_element(By.XPATH, '//*[@id="id_interest_2_bio"]')
interest2_bio_field.clear()
interest2_bio_field.send_keys('i am a professional photographer')
#link 2
interest2_link = driver.find_element(By.XPATH, '//*[@id="id_interest_2_link"]')
interest2_link.clear()
interest2_link.send_keys('https://www.dailysabah.com/gallery/worlds-most-popular-cat-breeds/images')


#bio3
interest3_bio_field = driver.find_element(By.XPATH, '//*[@id="id_interest_3_bio"]')
interest3_bio_field.clear()
interest3_bio_field.send_keys('I like to dance')
#link 3
interest3_link = driver.find_element(By.XPATH, '//*[@id="id_interest_3_link"]')
interest3_link.clear()
interest3_link.send_keys('https://www.dreamstime.com/illustration/dance.html')


#save(Successfully updated profile info!)
save_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
save_button.click()
time.sleep(2)

#serach
search = driver.find_element(By.XPATH, '/html/body/div/nav/div/ul/li[3]/a')
search.click()
time.sleep(2)

#search user
search_text = driver.find_element(By.XPATH, '//*[@id="id_search_text"]')
search_text.send_keys('19201048@uap-bd.edu')

search_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
search_button.click()
time.sleep(2)


#logout(You have successfully logged out)
logout = driver.find_element(By.XPATH, '/html/body/div/nav/div/ul/li[1]/a')
logout.click()
time.sleep(2)

#signup
signup = driver.find_element(By.XPATH, '/html/body/div/nav/div/ul/li[2]/a')
signup.click()
time.sleep(2)

