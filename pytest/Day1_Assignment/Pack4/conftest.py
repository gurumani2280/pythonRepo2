import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def precondition():
    print("This precondition will execute before the test method")
    driver = webdriver.Chrome()
    print("Chrome browser launched before starting testing")
    yield driver
    print("This statement will execute after test method execution")
    driver.quit()
    print("Chrome browser closed after testing")