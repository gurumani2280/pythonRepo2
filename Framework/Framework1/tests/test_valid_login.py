import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.login_page import LoginPage


@pytest.mark.usefixtures("precondition")
class TestValidLogin:
    @pytest.mark.pageclass
    def testValidLogin(self):
        print("This is testvalid login")
        lp=LoginPage(self.driver)
        lp.login("standard_user","secret_sauce")
        time.sleep(5)






