from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://en.wikipedia.org")
time.sleep(2)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scroll to bottom
time.sleep(2)
browser.execute_script("window.scrollTo(0,0)") #scroll to top
time.sleep(2)
browser.close()
