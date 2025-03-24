import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_teardown")
class Test_open_saucedemo:

    @pytest.mark.saucelogin
    def test_login(self):
        # login to website: www.saucedemo.com then logout.
        self.driver.get(url="https://www.saucedemo.com/v1/")
        print(self.driver.current_url, self.driver.title)  # Prints url and title
        print(self.driver.page_source)  # output: Entire page source(html output)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        print(self.driver.current_url, self.driver.title)
        self.driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(2)
        print(self.driver.current_url, self.driver.title)

'''
output:
(.venv) PS C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0> pytest -v -s .\\Day_0_test_0\\test_05.py
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 1 item                                                                                                                                                                                                                   

Day_0_test_0/test_05.py::Test_open_saucedemo::test_login
DevTools listening on ws://127.0.0.1:57920/devtools/browser/ba47c6c1-e9eb-4def-a191-eaeabc0bf9c2
[8444:10044:0321/065703.147:ERROR:device_event_log_impl.cc(202)] [06:57:03.147] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[8444:10044:0321/065703.272:ERROR:device_event_log_impl.cc(202)] [06:57:03.272] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
[8444:10044:0321/065703.527:ERROR:device_event_log_impl.cc(202)] [06:57:03.527] Display: display_layout.cc:556 PlacementList must be sorted by first 8 bits of display_id
https://www.saucedemo.com/v1/ Swag Labs
<html><head>
    <meta charset="UTF-8">
    <title>Swag Labs</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" type="text/css" href="css/sample-app-web.css">
    <link rel="icon" type="image/png" href="favicon.ico">
</head>
<body class="main-body">

<div class="login_logo"></div>

<div class="login_wrapper">

    <div class="login_wrapper-inner">

        <div id="login_button_container" class="form_column"><div class="login-box"><form><input type="text" class="form_input" data-test="username" id="user-name" name="user-name" placeholder="Username" autocorrect="off" autoca
pitalize="none" value=""><input type="password" class="form_input" data-test="password" id="password" name="password" placeholder="Password" autocorrect="off" autocapitalize="none" value=""><input type="submit" class="btn_action" id="login-button" value="LOGIN"></form></div></div>

        <img class="bot_column" src="img/Login_Bot_graphic.png">

    </div>
    <div class="login_credentials_wrap">
        <div class="login_credentials_wrap-inner">
            <div id="login_credentials" class="login_credentials">
                <h4>Accepted usernames are:</h4>
                standard_user<br>
                locked_out_user<br>
                problem_user<br>
                performance_glitch_user<br>

            </div>
            <div class="login_password">
                <h4>Password for all users:</h4>
                secret_sauce
            </div>
        </div>
    </div>
</div>
<script type="text/javascript" src="main.js"></script>

</body></html>
https://www.saucedemo.com/v1/inventory.html Swag Labs
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
https://www.saucedemo.com/v1/index.html Swag Labs
PASSED
'''