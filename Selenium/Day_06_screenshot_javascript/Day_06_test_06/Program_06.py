from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Filling all the details in html using XPATH
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)
#driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("RAHUL")
#time.sleep(1)
jsCode="document.getElementById('firstname').value='admin'"
driver.execute_script(jsCode)
time.sleep(2)
driver.quit()

#Note: Search on how to enable graded out tab