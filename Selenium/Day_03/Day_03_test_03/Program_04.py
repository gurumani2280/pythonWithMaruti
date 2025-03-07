from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)

state_element = driver.find_element(By.CSS_SELECTOR, 'select[name="alloptions"]')
dropdown = Select(state_element)
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_value('3')
time.sleep(1)
dropdown.select_by_visible_text("FOUR")
time.sleep(1)
dropdown.deselect_by_index(1)
time.sleep(3)

print(dropdown.is_multiple) #output: True
all_options = dropdown.options
print(len(all_options)) #output: 5

for option in all_options:
    print(option.text)
    print(option.get_attribute("value"))
driver.quit()

'''
output:
ONE
1
TWO
2
THREE
3
FOUR
4
FIVE
5
'''

