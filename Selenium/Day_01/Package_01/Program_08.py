import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome() #opened a chrome browser
time.sleep(2) #It pauses the execution for 5 seconds
driver.maximize_window() #This will maximize the window.
time.sleep(2)
driver.get("https://www.google.com/") #Opening a URL
time.sleep(2)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("facebook", Keys.ENTER)
time.sleep(2)


print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser
