from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
parent_window_Handle = driver.current_window_handle
print(parent_window_Handle)
all_Window_Handle = driver.window_handles

driver.find_element(By.XPATH,"//a/button[contains(text(), 'click ')]").click()
time.sleep(3)
all_Window_Handle = driver.window_handles
print(all_Window_Handle)
print(len(all_Window_Handle))
child_window_handle = all_Window_Handle[1]
print(child_window_handle)
time.sleep(3)
driver.quit()

'''
output:
5A35959A73A6DE68CA36FE0D995F1A58
['5A35959A73A6DE68CA36FE0D995F1A58', 'D047E41C5532D5F678C14DE7259FDC88']
2
D047E41C5532D5F678C14DE7259FDC88
'''