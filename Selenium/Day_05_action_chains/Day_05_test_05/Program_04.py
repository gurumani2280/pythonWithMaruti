from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(4)
double_click_button = driver.find_element(By.XPATH, "//button[text() = 'Double-Click Me To See Alert']")
action = ActionChains(driver)
action.double_click(double_click_button).perform()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()