import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def precondition(request):
    print("This precondition will execute before the test method")
    driver = webdriver.Chrome()
    print("Chrome browser launched before starting testing")
    request.cls.driver=driver
    yield
    print("This statement will execute after test method execution")
    driver.quit()
    print("Chrome browser closed after testing")