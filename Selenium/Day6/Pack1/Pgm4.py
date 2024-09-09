from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {"download.default_directory": r"E:\Sony\Emexo\Downloads\\", # IMPORTANT - ENDING SLASH V IMPORTANT
                "directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
#driver=webdriver.Chrome()
#driver.maximize_window()
time.sleep(2)
driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
time.sleep(2)
course_location = driver.find_element(By.LINK_TEXT, "Enabled")
action = ActionChains(driver)
action.move_to_element(course_location).perform()
time.sleep(3)
download_button = driver.find_element(By.LINK_TEXT, "Downloads")
action.move_to_element(download_button).perform()
time.sleep(3)
#driver.find_element(By.LINK_TEXT,"PDF").click()
#driver.find_element(By.LINK_TEXT,"CSV").click()
driver.find_element(By.LINK_TEXT,"Excel").click()
time.sleep(3)

