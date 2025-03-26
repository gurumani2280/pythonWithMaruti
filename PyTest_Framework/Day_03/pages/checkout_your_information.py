from pages.base_page import BasePage
from pages.checkout_your_information_locators import CheckoutYourInformationLocators


class CheckoutYourInformation(BasePage, CheckoutYourInformationLocators):
    def __init__(self, driver):
        self.driver = driver

    def get_firstname(self):
        return self.driver.find_element(*self.first_name)

    def get_lastname(self):
        return self.driver.find_element(*self.last_name)

    def get_postalcode(self):
        return self.driver.find_element(*self.postal_code)

    def continue_button(self, firstname, lastname, postalcode):
        self.get_firstname().send_keys(firstname)
        self.get_lastname().send_keys(lastname)
        self.get_postalcode().send_keys(postalcode)
        self.continue_button().click()





