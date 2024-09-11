from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(2)
testing_checkbox=driver.find_element(By.CSS_SELECTOR,"input[value='testing']")
#testing_checkbox.click()
time.sleep(2)
print(testing_checkbox.is_selected())
if testing_checkbox.is_selected():
    print("Check box is already selected, not clicking again")
else:
    print("Unchecked, so clicking again")
    testing_checkbox.click()
time.sleep(2)
print(testing_checkbox.is_selected())
driver.quit()
"""
False
Unchecked, so clicking again
True
"""