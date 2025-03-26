from pages.base_page import BasePage
from pages.your_cart_page_locators import YourCartPageLocators


class YourCart(BasePage, YourCartPageLocators):
    def __init__(self, driver):
        self.driver = driver

    def get_checkout(self):
        return self.driver.find_element(*self.checkout_button_locator)
    
    def checkout(self):
        self.get_checkout().click()