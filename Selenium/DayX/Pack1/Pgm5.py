#forward/back/refresh a tab
import time
from selenium import webdriver
driver=webdriver.Chrome()
time.sleep(5)#delay
driver.maximize_window()
time.sleep(5)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(5)
driver.get("https://www.google.com/")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()