from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url="file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(2)
driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("test user") #user name = test user
time.sleep(2)
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("password123") #user name = password123
time.sleep(2)
driver.quit()

#Assignment: Add all the details using XPATH only.
#https://opensource-demo.orangehrmlive.com --> Try for this website also.