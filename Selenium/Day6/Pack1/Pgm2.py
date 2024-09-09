from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
time.sleep(2)
course_location = driver.find_element(By.LINK_TEXT, "Enabled")
action = ActionChains(driver)
action.move_to_element(course_location).perform()
time.sleep(3)
back_to_JqueryButton=driver.find_element(By.LINK_TEXT,"Back to JQuery UI")
action.move_to_element(back_to_JqueryButton).perform()
driver.quit()
