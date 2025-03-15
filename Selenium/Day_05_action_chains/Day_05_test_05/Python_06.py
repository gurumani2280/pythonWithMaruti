from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import fail_request
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/index.html")
time.sleep(4)
block_1 = driver.find_element(By.XPATH, "//h1[text() = 'Block 1']")
block_3 = driver.find_element(By.XPATH, "//h1[text() = 'Block 3']")
action = ActionChains(driver)
action.drag_and_drop(block_1,block_3).perform()
time.sleep(3)
driver.quit()


'''
#Assignment:
driver.get()
windows.maximize()

webdriver() used so far?
webelement() -> click. send_keys used so far?
select_class() used so far?
switch_to_alert() used so far?
actionschains() used so far?
by class variables
Note: along with imports
'''