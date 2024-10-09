from selenium.webdriver.common.by import By


class LoginPageLocator:
    user_name_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
    error_message_locator = (By.TAG_NAME, "h3")
