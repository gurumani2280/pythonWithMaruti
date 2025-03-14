from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#login to website: www.saucedemo.com then logout.
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "https://www.saucedemo.com/v1/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)
driver.quit()















