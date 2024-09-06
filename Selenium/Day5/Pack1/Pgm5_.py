from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)
driver.find_element(By.XPATH,"//button[text() = 'Click for JS Alert']").click()
time.sleep(3)
js_alert=driver.switch_to.alert
print(js_alert.text)#I am a JS Alert
js_alert.accept()
time.sleep(3)
result=driver.find_element(By.ID,"result")
print(result.text)#You successfully clicked an alert
driver.quit()
