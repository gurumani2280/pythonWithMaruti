from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "https://www.saucedemo.com/v1/")
print(driver.current_url, driver.title)
print(driver.page_source) #output: Entire page source(htmp output)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
print(driver.current_url, driver.title)
driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)
print(driver.current_url, driver.title)
driver.quit()

'''
output:
https://www.saucedemo.com/v1/ Swag Labs
https://www.saucedemo.com/v1/inventory.html Swag Labs
https://www.saucedemo.com/v1/index.html Swag Labs
'''
#Note: Read "how selenium communicate with browser"











