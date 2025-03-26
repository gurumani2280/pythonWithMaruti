import time

from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators
from pages.products_page_locators import ProductsPageLocators
from utilities.selenium_utilities import SeleniumUtilities


class ProductsPage(BasePage, ProductsPageLocators):
    def __init__(self, driver):
        self.driver = driver

    def get_open_menu(self):
        #return self.driver.find_element(*self.open_menu_button_locator)
        return SeleniumUtilities.wait_for_element_to_be_displayed(self.driver, self.open_menu_button_locator)

    def get_logout(self):
        #return self.driver.find_element(*self.logout_link_locator)
        return SeleniumUtilities.wait_for_element_to_be_clickable(self.driver, self.logout_link_locator)

    def logout(self):
        self.get_open_menu().click()
        #time.sleep(2)
        self.get_logout().click()





