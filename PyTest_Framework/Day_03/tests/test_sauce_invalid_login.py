import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.login_page import LoginPage


#@pytest.mark.usefixtures("setup_teardown")
class Test_invalid_saucedemo:

    @pytest.mark.saucelogin
    def test_invalid_login(self):
        # login to website: www.saucedemo.com then logout.
        lp = LoginPage(self.driver)
        lp.login("Problem1_user", "Invalid_password")
        error_message = lp.get_error_message_text()
        print(error_message)


'''
output:
'''