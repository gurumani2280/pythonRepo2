import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("precondition")
class TestBasic2:
    def test1(self):
        print("This is test1 method")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get("https://www.saucedemo.com/v1/")
        time.sleep(5)
        uname_field = self.driver.find_element(By.ID, "user-name")
        uname_field.send_keys("standard_user")
        time.sleep(5)
        pwd_field = self.driver.find_element(By.ID, "password")
        pwd_field.send_keys("secret_sauce")
        time.sleep(5)
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(5)






    