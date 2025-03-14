#Opening Edge browser

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Program to search facebook using Edge browser
driver=webdriver.Edge() #opened a Edge browser
time.sleep(2) #It pauses the execution for 5 seconds
driver.maximize_window() #This will maximize the window.
time.sleep(2)
driver.get("https://www.google.com/") #Opening a URL
time.sleep(2)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("facebook")
time.sleep(2)
search_button = driver.find_element(By.NAME, "btnK")
search_button.click()
time.sleep(2)

print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser
