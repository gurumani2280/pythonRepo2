from pages.login_page_locators import LoginPageLocator


class LoginPage(LoginPageLocator):
    def __init__(self,driver):
        self.driver=driver
    def get_username(self):
        return self.driver.find_element(*self.user_name_locator)
    def get_password(self):
        return self.driver.find_element(*self.password_locator)
    def get_login_button(self):
        return self.driver.find_element(*self.login_button_locator)
    def get_error_message(self):
        return self.driver.find_element(*self.error_message_locator)
    def login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login_button().click()
    def get_error_msg(self):
        return self.get_error_message().text
