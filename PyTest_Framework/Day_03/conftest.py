from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="class", autouse=True)
def setup_teardown(request): #request is a built in fixture
    print("This will run before the test_feature1 method")
    driver = webdriver.Chrome()  # opened a chrome browser
    driver.implicitly_wait(10) #when the locator or element isn ot available then it will wait till it is available
    driver.maximize_window()  # This will maximize the window.
    driver.get(url="https://www.saucedemo.com/v1/")
    request.cls.driver = driver
    yield
    print("This will run after the test_feature1 method")
    driver.quit()  # Quit will close the browser