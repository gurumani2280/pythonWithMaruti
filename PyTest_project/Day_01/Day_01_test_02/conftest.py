from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="class")
def setup_teardown(request):
    print("This will run before the test_feature1 method")
    driver = webdriver.Chrome()  # opened a chrome browser
    time.sleep(2)  # It pauses the execution for 5 seconds
    driver.maximize_window()  # This will maximize the window.
    time.sleep(2)
    request.cls.driver = driver
    yield
    print("This will run after the test_feature1 method")
    driver.quit()  # Quit will close the browser