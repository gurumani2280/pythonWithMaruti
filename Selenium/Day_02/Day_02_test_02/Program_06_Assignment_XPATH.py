from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Filling all the details in html using XPATH
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url = "file:///C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Rahul_B")
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("test123")
time.sleep(1)
#driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("RAHUL")
#time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("BHATIA")
time.sleep(1)
driver.find_element(By.XPATH, '//textarea[@name="address"]').send_keys("#123, 2nd Cross, Bangalore-560050")
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="m"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="dob"]').send_keys("07/03/2025")
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="selenium"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="testing"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="java"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//select[@name="state"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//option[@value="0"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//select[@name="alloptions"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//option[@value="1"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="resume"]').send_keys("C:/Users/USER/Desktop/python_repository/pythonWithMaruti/Selenium/BasicHtmlElement.html")
time.sleep(2)
driver.find_element(By.XPATH, '//a[@title="googleLink"]').click()
time.sleep(1)
driver.back()
element_image = driver.find_element(By.XPATH, "//img") #For XPATH // is mandatory
print(element_image.is_enabled())
print(element_image.is_displayed())
print(element_image.is_selected())
print(element_image.get_attribute("src"))
print(element_image.get_attribute("alt"))
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(1)
print("Details entered")
driver.quit()

'''
output"
True
True
False
https://www.w3schools.com/images/w3schools_green.jpg
W3Schools.com
Details entered
'''

#(//option[@value="1"])[2] -> To select second occurance