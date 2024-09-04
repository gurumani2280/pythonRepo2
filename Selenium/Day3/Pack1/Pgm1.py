from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(10)
username_field=driver.find_element(By.NAME,"username")
print(username_field.get_attribute("type"))
driver.quit()
print(username_field.get_attribute('placeholder'))
print('value of username field: ',username_field.get_attribute('value'))
time.sleep(2)
username_field.send_keys("Kayal")
print('value of username field: ',username_field.get_attribute('value'))
time.sleep(2)
username_field.send_keys("payal")
print('value of username field: ',username_field.get_attribute('value'))
time.sleep(2)
username_field.clear()
username_field.send_keys("payal")
print('value of username field: ',username_field.get_attribute('value'))
driver.quit()
