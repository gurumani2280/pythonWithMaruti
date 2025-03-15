from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(4)
right_click_button = driver.find_element(By.XPATH, "//span[text() = 'right click me']")
action = ActionChains(driver)
action.context_click(right_click_button).perform() #context_click() is for right click
time.sleep(3)
driver.find_element(By.XPATH,"//span[text() = 'Quit']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()