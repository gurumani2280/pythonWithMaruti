from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(url="file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)
wait = WebDriverWait(driver, 20) #wait time is 20 seconds

login_button = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="Login"]'))) #This will wait till the locator is visible
login_button.click()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="BackToLoginPage"]').click()
time.sleep(1)
print("Details entered")
driver.quit()