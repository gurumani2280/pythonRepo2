from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(5)
all_checkboxes=driver.find_element(By.NAME,"skill")
print("type",type(all_checkboxes))
print(len(all_checkboxes))
all_checkboxes[2].click()
time.sleep(5)
driver.quit()