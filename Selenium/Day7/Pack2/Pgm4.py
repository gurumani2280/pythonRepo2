from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Monisha/Documents/HTML_Selenium/BasicHtmlElement.html")
time.sleep(2)
disable_textbox = driver.find_element(By.ID,"firstname")

driver.execute_script("arguments[0].value='Kayal';", disable_textbox)#Javascript click 3rd way of clicking
time.sleep(3)
driver.quit()


