
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
parent_window_Handle = driver.current_window_handle
print(parent_window_Handle)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
#print(type(all_Window_Handle))
print(len(all_Window_Handle))

#driver.find_element(By.XPATH,"//a/button[contains(text(), 'click ')]").click()
driver.switch_to.new_window('tab')#tab is a keyword
time.sleep(4)
driver.get("https://www.w3schools.com/")
time.sleep(3)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
#print(type(all_Window_Handle))
print(len(all_Window_Handle))
driver.close()
time.sleep(4)
driver.switch_to.window(parent_window_Handle)
time.sleep(4)
driver.find_element(By.XPATH,"//a/button[contains(text(), 'click ')]").click()
time.sleep(4)
driver.close()
time.sleep(4)
driver.quit()