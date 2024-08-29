#Invalid username and password
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(5)#delay
driver.maximize_window()
time.sleep(5)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(5)
uname_field=driver.find_element(By.ID,"user-name")
uname_field.send_keys("Sony")
time.sleep(5)
pwd_field=driver.find_element(By.ID,"password")
pwd_field.send_keys("Test@123")
time.sleep(5)
login_btn=driver.find_element(By.ID,"login-button")
login_btn.click()
time.sleep(5)
driver.quit()