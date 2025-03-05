import time
from selenium import webdriver

driver=webdriver.Chrome() #opened a chrome browser
time.sleep(5) #It pauses the execution for 5 seconds
print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser