import time
from selenium import webdriver

driver=webdriver.Chrome() #opened a chrome browser
time.sleep(2) #It pauses the execution for 5 seconds
driver.maximize_window() #This will maximize the window.
time.sleep(5)
# driver.maximize_window() #second time maximize will not work in Selenium/Automation
# time.sleep(5)
driver.minimize_window() #This will minimize the window.
time.sleep(5)
print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser
