from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://pythonspot.com")
time.sleep(3)
#driver.save_screenshot("PythonScreenshot.png")
header_element=driver.find_element(By.CSS_SELECTOR,"div.head")
header_element.screenshot("header.png")
driver.quit()


