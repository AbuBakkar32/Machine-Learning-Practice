from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
browser.maximize_window()


browser.get("http://studentportal.diu.edu.bd/#/dashboard")
browser.find_element_by_id('email').send_keys()
browser.find_element_by_id('pass').send_keys()
browser.find_element_by_name('login').click()

time.sleep(2)

# browser.close()
# browser.quit()
print('Thank for logged-in our website')