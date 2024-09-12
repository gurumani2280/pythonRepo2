from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://pythonbasics.org/")
time.sleep(3)
js="alert('Hello World')"
driver.execute_script(js)
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(4)
driver.quit()


