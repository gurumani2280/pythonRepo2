from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///E:/Sony/Emexo/Project2_Selenium/sample/Demo1.html")
parent_window_Handle = driver.current_window_handle
print(parent_window_Handle)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
#print(type(all_Window_Handle))
print(len(all_Window_Handle))

#driver.find_element(By.XPATH,"//a/button[contains(text(), 'click ')]").click()
driver.switch_to.new_window('window')
time.sleep(3)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
#print(type(all_Window_Handle))
print(len(all_Window_Handle))
time.sleep(4)
driver.close()
time.sleep(4)
driver.quit()