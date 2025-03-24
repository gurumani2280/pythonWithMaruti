from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestHtml:
    def test_html_using_CSS_SELECTOR(self):
        # Filling all the details in html using CSS_SELECTOR
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(
            url="file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys("Rahul_B")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("test123")
        time.sleep(1)
        # driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys("RAHUL")
        # time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys("BHATIA")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'textarea[name="address"]').send_keys("#123, 2nd Cross, Bangalore-560050")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[value="m"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[name="dob"]').send_keys("07/03/2025")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[value="selenium"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[value="testing"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[value="java"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'select[name="state"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'option[value="1"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'select[name="alloptions"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'option[value="1"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input[name="resume"]').send_keys(
            "C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'a[title="googleLink"]').click()
        time.sleep(1)
        driver.back()
        element_image = driver.find_element(By.CSS_SELECTOR, "img")
        print(element_image.is_enabled())
        print(element_image.is_displayed())
        print(element_image.is_selected())
        print(element_image.get_attribute("src"))
        print(element_image.get_attribute("alt"))
        driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()
        time.sleep(1)
        print("Details entered")
        driver.quit()

    def test_html_using_XPATH(self):
        # Filling all the details in html using XPATH
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(
            url="file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Rahul_B")
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("test123")
        time.sleep(1)
        # driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("RAHUL")
        # time.sleep(1)
        driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("BHATIA")
        time.sleep(1)
        driver.find_element(By.XPATH, '//textarea[@name="address"]').send_keys("#123, 2nd Cross, Bangalore-560050")
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="m"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@name="dob"]').send_keys("07/03/2025")
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="selenium"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="testing"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="java"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//select[@name="state"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//option[@value="0"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//select[@name="alloptions"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//option[@value="1"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@name="resume"]').send_keys(
            "C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
        time.sleep(2)
        driver.find_element(By.XPATH, '//a[@title="googleLink"]').click()
        time.sleep(1)
        driver.back()
        element_image = driver.find_element(By.XPATH, "//img")  # For XPATH // is mandatory
        print(element_image.is_enabled())
        print(element_image.is_displayed())
        print(element_image.is_selected())
        print(element_image.get_attribute("src"))
        print(element_image.get_attribute("alt"))
        driver.find_element(By.XPATH, '//input[@value="Login"]').click()
        time.sleep(1)
        print("Details entered")
        driver.quit()


'''
output:
(.venv) PS C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0> pytest -v -s .\\Day_0_test_0\\test_06.py
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 2 items                                                                                                                                                                                                                  

Day_0_test_0/test_06.py::TestHtml::test_html_using_CSS_SELECTOR
DevTools listening on ws://127.0.0.1:58011/devtools/browser/d1ee9a22-7f80-45d0-904a-022374f3bbfc
[12416:13396:0321/065958.064:ERROR:device_event_log_impl.cc(202)] [06:59:58.064] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[12416:13396:0321/065958.206:ERROR:device_event_log_impl.cc(202)] [06:59:58.206] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[12416:13396:0321/065958.245:ERROR:device_event_log_impl.cc(202)] [06:59:58.246] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
[12416:13396:0321/070016.796:ERROR:interface_endpoint_client.cc(725)] Message 1 rejected by interface blink.mojom.WidgetHost
True
True
False
https://www.w3schools.com/images/w3schools_green.jpg
W3Schools.com
Details entered
PASSED
Day_0_test_0/test_06.py::TestHtml::test_html_using_XPATH
DevTools listening on ws://127.0.0.1:58046/devtools/browser/b5b7b838-8d50-426d-9824-b7928b0ccc5b
[15820:13972:0321/070023.731:ERROR:device_event_log_impl.cc(202)] [07:00:23.731] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[15820:13972:0321/070023.904:ERROR:device_event_log_impl.cc(202)] [07:00:23.904] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[15820:13972:0321/070023.925:ERROR:device_event_log_impl.cc(202)] [07:00:23.924] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
[15820:13972:0321/070042.086:ERROR:interface_endpoint_client.cc(725)] Message 1 rejected by interface blink.mojom.WidgetHost
True
True
False
https://www.w3schools.com/images/w3schools_green.jpg
W3Schools.com
Details entered
PASSED

'''