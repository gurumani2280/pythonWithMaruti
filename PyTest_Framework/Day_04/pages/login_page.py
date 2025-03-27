from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators
from utilities.selenium_utilities import SeleniumUtilities


class LoginPage(BasePage, LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        #return self.driver.find_element(*self.username_locator) #This is to untuple the tuple -> this is without wait time
        return SeleniumUtilities.wait_for_element_to_be_displayed(self.driver, self.username_locator) #This is with wait time.

    def get_password(self):
        #return self.driver.find_element(*self.password_locator) #This is without wait time
        return SeleniumUtilities.wait_for_element_to_be_displayed(self.driver, self.password_locator)

    def get_login(self):
        #return self.driver.find_element(*self.login_button_locator)
        return SeleniumUtilities.wait_for_element_to_be_displayed(self.driver, self.login_button_locator)


    def get_error_message(self):
        #return self.driver.find_element(*self.error_message_locator)
        return SeleniumUtilities.wait_for_element_to_be_displayed(self.driver, self.error_message_locator)

    def login(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()

    def get_error_message_text(self):
        return self.get_error_message().text





