from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window();
driver.get('https://pythonspot.com')
#driver.save_screenshot("screenshot.png")
driver.get_screenshot_as_file("screenshot3.png")

element = driver.find_element(By.CSS_SELECTOR, 'div.head')
element.screenshot('just-the-header1.png')
element = driver.find_element(By.XPATH, '//h1[@class="post-title"]')
element.screenshot('just-the-header2.png')
driver.close()
