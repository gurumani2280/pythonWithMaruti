from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(url="file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="BackToLoginPage"]').click()
time.sleep(1)
print("Details entered")
driver.quit()