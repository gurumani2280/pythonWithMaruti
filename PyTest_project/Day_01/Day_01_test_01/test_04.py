import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
class TestBasic:

    @pytest.mark.basic02
    def test_basics(self):
        self.driver.get("https://www.google.com/")  # Opening a URL
        time.sleep(2)
        self.driver.get("https://www.saucedemo.com/v1/")  # Opening a new URL
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.forward()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        print("Sleep completed and program execution completed")

    @pytest.mark.basic02
    def test_google_search(self):
        self.driver.get("https://www.google.com/") #Opening a URL
        time.sleep(2)
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("facebook", Keys.ENTER)
        time.sleep(2)
        print("Sleep completed and program execution completed")

    @pytest.fixture(scope="class")
    def setup_teardown(self, request):
        print("This will run before the test_feature1 method")
        #global driver #To make driver variable global.
        driver = webdriver.Chrome()  # opened a chrome browser
        time.sleep(2)  # It pauses the execution for 5 seconds
        driver.maximize_window()  # This will maximize the window.
        time.sleep(2)
        request.cls.driver = driver
        yield
        print("This will run after the test_feature1 method")
        driver.quit()  # Quit will close the browser

'''
pytest -v -s .\\Day_0_test_0\\test_03.py
output:
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 2 items                                                                                                                                                                                                                  

Day_0_test_0/test_03.py::TestBasic::test_basics
DevTools listening on ws://127.0.0.1:56507/devtools/browser/e047af51-4291-4acc-b039-166f879d14d6
[22028:13612:0320/075833.586:ERROR:device_event_log_impl.cc(202)] [07:58:33.586] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[22028:13612:0320/075833.970:ERROR:device_event_log_impl.cc(202)] [07:58:33.971] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[22028:13612:0320/075834.059:ERROR:device_event_log_impl.cc(202)] [07:58:34.060] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
Sleep completed and program execution completed
PASSED
Day_0_test_0/test_03.py::TestBasic::test_google_search
DevTools listening on ws://127.0.0.1:56551/devtools/browser/f2e60ae9-a12f-4d8b-a3fa-e286ac49fc2c
[14196:11936:0320/075854.456:ERROR:device_event_log_impl.cc(202)] [07:58:54.456] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[14196:11936:0320/075854.746:ERROR:device_event_log_impl.cc(202)] [07:58:54.747] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[14196:11936:0320/075854.794:ERROR:device_event_log_impl.cc(202)] [07:58:54.794] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
Sleep completed and program execution completed
PASSED
'''