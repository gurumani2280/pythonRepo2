from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(2)
testing_checkbox = driver.find_element(By.XPATH, "//input[@value = 'testing']")

driver.execute_script("arguments[0].click()", testing_checkbox)#Javascript click 3rd way of clicking
time.sleep(3)
driver.quit()


