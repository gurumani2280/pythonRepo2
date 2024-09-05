#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/BasicHtmlElement.html")
time.sleep(3)
state_dropdown=driver.find_element(By.NAME,"state")
sel=Select(state_dropdown)
sel.select_by_index(1)
time.sleep(3)
sel.select_by_value("2")
time.sleep(3)
sel.select_by_visible_text("TELENGANA")
time.sleep(3)
print(sel.is_multiple)
option_list=sel.options
for option in option_list:
    print(option.text)
    print(option.get_attribute("value"))
driver.quit()
