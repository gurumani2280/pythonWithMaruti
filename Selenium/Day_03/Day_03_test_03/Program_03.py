from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)

state_element = driver.find_element(By.CSS_SELECTOR, 'select[name="state"]')
dropdown = Select(state_element)
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_value('2')
time.sleep(1)
dropdown.select_by_visible_text("KARNATAKA")
time.sleep(1)
dropdown.select_by_index(4)
time.sleep(1)
print(dropdown.is_multiple) #output: None
all_options = dropdown.options
print(len(all_options)) #output: 5

for option in all_options:
    print(option.text)
    print(option.get_attribute("value"))
driver.quit()

'''
output:
5
SELECT
0
KARNATAKA
1
ANDHRA
2
TELENGANA
3
TAMILNADU
4
'''

