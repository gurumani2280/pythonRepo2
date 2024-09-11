from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(2)
first_nametxtbox=driver.find_element(By.ID,"firstname")
time.sleep(2)
print(first_nametxtbox.is_enabled())
if first_nametxtbox.is_enabled():
    print("Test box is enabled, enter the text")
    first_nametxtbox.send_keys("Aman")
else:
    print("Text box is disabled, unable to enter")
time.sleep(2)
driver.quit()

"""
False
Text box is disabled, unable to enter
"""
