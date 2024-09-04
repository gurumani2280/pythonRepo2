from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(5)
all_checkboxes=driver.find_elements(By.TAG_NAME,"option")
print("type",type(all_checkboxes))
print(len(all_checkboxes))
for element in all_checkboxes:
    print(element.text)
    time.sleep(2)
time.sleep(2)
driver.quit()