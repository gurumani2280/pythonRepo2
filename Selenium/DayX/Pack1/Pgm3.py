#Maximise/minimise a window
import time

from selenium import webdriver
driver=webdriver.Chrome()
time.sleep(5)#delay
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.quit()