from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url="file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)

all_inputs = driver.find_elements(By.CSS_SELECTOR,'input')
print(len(all_inputs), type(all_inputs))  # output: 3 <class 'list'>
for input in all_inputs:
    print(input.get_attribute("type"))
    time.sleep(1)

driver.quit()

'''
output:
13 <class 'list'>
text
password
text
text
radio
radio
text
checkbox
checkbox
checkbox
file
submit
reset

'''

