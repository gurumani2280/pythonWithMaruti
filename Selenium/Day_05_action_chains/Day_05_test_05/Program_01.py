import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
time.sleep(3)
# get element
element = driver.find_element(By.XPATH,"//div[text()='Courses']")

# create action chain object
action = ActionChains(driver)

# click the item
#action.click(on_element = element) #This is to click the element
action.move_to_element(element)

# perform the operation
action.perform()
time.sleep(3)
driver.quit()
