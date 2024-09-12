from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(4)
about_us_text = driver.find_element(By.XPATH, "//h5[text()='About us']")
driver.execute_script("arguments[0].scrollIntoView();", about_us_text)
time.sleep(3)
driver.quit()

