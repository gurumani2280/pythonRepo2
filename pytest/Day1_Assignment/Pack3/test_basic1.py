import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test1(precondition):
    print("This is test1 method")
    print("Precondition ", precondition)
    driver = precondition
    time.sleep(5)  # delay
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(5)
    uname_field = driver.find_element(By.ID, "user-name")
    uname_field.send_keys("abc")
    time.sleep(5)
    pwd_field = driver.find_element(By.ID, "password")
    pwd_field.send_keys("Test123")
    time.sleep(5)
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    time.sleep(5)
    error_msg_element = driver.find_element(By.TAG_NAME, "h3")
    error_msg_text = error_msg_element.text
    print(error_msg_text)  # Epic sadface: Username and password do not match any user in this service





    