from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
parent_window_Handle = driver.current_window_handle
print(parent_window_Handle)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
print(type(all_Window_Handle))
print(len(all_Window_Handle))

driver.find_element(By.XPATH,"//a/button[contains(text(), 'click ')]").click()
time.sleep(3)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
print(type(all_Window_Handle))
print(len(all_Window_Handle))
child_window_handle = all_Window_Handle[1]
print(child_window_handle)
driver.switch_to.window(child_window_handle)
time.sleep(3)
driver.find_element(By.XPATH, "//span[text() = 'Documentation']").click()
time.sleep(3)
driver.switch_to.window(parent_window_Handle)
driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]").click()
time.sleep(3)