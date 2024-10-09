import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.login_page import LoginPage


@pytest.mark.usefixtures("precondition")
class TestInValidLogin:
    @pytest.mark.pageclass
    def testInValidLogin(self):
        print("This is testinvalid login")
        lp=LoginPage(self.driver) # lp -> Login page object
        lp.login("test","Test@123")
        time.sleep(5)
        print("Error message",lp.get_error_message())






