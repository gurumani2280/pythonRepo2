from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://pythonbasics.org/")
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#vertical scroll
time.sleep(3)
driver.execute_script('window.scrollTo(0,0)')
time.sleep(3)
driver.quit()


