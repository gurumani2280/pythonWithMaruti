import time
from selenium import webdriver

#Opening Firefox browser
driver=webdriver.Firefox() #opened a firefox browser
time.sleep(5) #It pauses the execution for 5 seconds
print("Sleep completed and program execution completed")
driver.quit() #Quit will close the browser

'''
output:
Sleep completed and program execution completed
'''