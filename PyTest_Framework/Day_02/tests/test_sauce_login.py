import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("setup_teardown")
class Test_open_saucedemo:

    @pytest.mark.saucelogin
    def test_login(self):
        # login to website: www.saucedemo.com then logout.
        lp = LoginPage(self.driver)
        print(lp.get_page_title(), lp.get_page_url())
        lp.login("standard_user", "secret_sauce")
        pp = ProductsPage(self.driver)
        print(pp.get_page_title(), pp.get_page_url())
        pp.logout()
        print(lp.get_page_title(), lp.get_page_url())

'''
output:
'''