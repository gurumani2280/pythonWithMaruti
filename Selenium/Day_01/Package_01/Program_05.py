import time
from selenium import webdriver

driver=webdriver.Chrome() #opened a chrome browser
time.sleep(2) #It pauses the execution for 5 seconds
driver.maximize_window() #This will maximize the window.
time.sleep(2)
driver.get("https://www.google.com/") #Opening a URL
time.sleep(2)
driver.get("https://www.saucedemo.com/v1/") #Opening a new URL
time.sleep(2)
driver.get("www.saucedemo.com/v1/") #Opening a new URL
time.sleep(2)
print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser
