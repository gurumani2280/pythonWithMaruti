from selenium import webdriver
import time

#Opening Chrome browser
driver=webdriver.Chrome() #opened a chrome browser
time.sleep(5) #It pauses the execution for 5 seconds
print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser

'''
output:
Sleep completed and program execution completed
'''