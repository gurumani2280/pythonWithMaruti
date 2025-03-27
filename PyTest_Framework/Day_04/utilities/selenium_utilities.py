from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#https://selenium-python.readthedocs.io/waits.html -> below code is copied from this website
class SeleniumUtilities:
    @staticmethod
    def wait_for_element_to_be_displayed(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

