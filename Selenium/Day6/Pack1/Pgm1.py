from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.geeksforgeeks.org/")
time.sleep(2)
course_location = driver.find_element(By.XPATH, "//div[text() = 'Courses']")
action = ActionChains(driver)
action.move_to_element(course_location).perform()
time.sleep(3)
driver.quit()
