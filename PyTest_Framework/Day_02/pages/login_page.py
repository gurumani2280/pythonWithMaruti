from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(*self.username_locator) #This is to untuple the tuple

    def get_password(self):
        return self.driver.find_element(*self.password_locator)

    def get_login(self):
        return self.driver.find_element(*self.login_button_locator)

    def get_error_message(self):
        return self.driver.find_element(*self.error_message_locator)

    def login(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()

    def get_error_message_text(self):
        return self.get_error_message().text





