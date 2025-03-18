import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://pythonbasics.org")
js = 'alert("Hello World")' #this is javascript code
driver.execute_script(js) #It will generate alerts
time.sleep(2)
driver.quit()