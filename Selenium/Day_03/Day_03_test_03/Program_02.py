from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)

#driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
#Note: find_element() will always give the first matching element when multiple options are available
all_check_boxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]') #find_elements -> returns multiple elements+
print(len(all_check_boxes), type(all_check_boxes)) #output: 3 <class 'list'>
for check_box in all_check_boxes:
    check_box.click()
    time.sleep(1)

#To handle exception: Where element is not find
all_check_boxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox123"]') #find_elements -> returns list with length(0)
print(len(all_check_boxes), type(all_check_boxes)) #output: 0 <class 'list'>

driver.quit()

