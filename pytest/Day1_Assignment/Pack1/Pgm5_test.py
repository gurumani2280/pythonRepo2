import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestSample:
    @pytest.mark.cssselector
    def testsamplemethod(self):
        print("This is a sample class")

        driver = webdriver.Chrome()
        time.sleep(5)  # delay
        driver.maximize_window()
        time.sleep(5)
        driver.get("https://www.saucedemo.com/v1/")
        time.sleep(5)
        uname_field = driver.find_element(By.ID, "user-name")
        uname_field.send_keys("standard_user")
        time.sleep(5)
        pwd_field = driver.find_element(By.ID, "password")
        pwd_field.send_keys("secret_sauce")
        time.sleep(5)
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(5)
        menu_button = driver.find_element(By.XPATH, "//button[text()='Open Menu']")
        menu_button.click()
        logout_link = driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()
        time.sleep(5)
        driver.quit()




