import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("precondition")
class TestBasic1:
    def test1(self):
        print("This is test1 method")
        time.sleep(5)  # delay
        self.driver.maximize_window()
        time.sleep(5)
        self.get("https://www.saucedemo.com/v1/")
        time.sleep(5)
        uname_field = self.driver.find_element(By.ID, "user-name")
        uname_field.send_keys("abc")
        time.sleep(5)
        pwd_field = self.driver.find_element(By.ID, "password")
        pwd_field.send_keys("Test123")
        time.sleep(5)
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(5)
        error_msg_element = self.driver.find_element(By.TAG_NAME, "h3")
        error_msg_text = error_msg_element.text
        print(error_msg_text)  # Epic sadface: Username and password do not match any user in this service






    