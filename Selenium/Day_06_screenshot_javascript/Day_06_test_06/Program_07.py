from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(4)
login_button = driver.find_element(By.XPATH, '//input[@value = "Login"]')
jsCode="arguments[0].click();"
driver.execute_script(jsCode, login_button)
time.sleep(3)


driver.quit()

