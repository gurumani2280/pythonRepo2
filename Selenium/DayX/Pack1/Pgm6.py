#get the title of a page
import time
from selenium import webdriver
driver=webdriver.Chrome()
time.sleep(5)#delay
driver.maximize_window()
time.sleep(5)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(5)
title_page=driver.title
page_url=driver.current_url
print(title_page)
print(page_url)
backend_html=driver.page_source
print(backend_html)
driver.get("file:///C:/Users/Amaljith%20TM/Desktop/demo.html")
time.sleep(5)
title_page=driver.title
page_url=driver.current_url
print(title_page)
print(page_url)
backend_html=driver.page_source
print(backend_html)
driver.quit()