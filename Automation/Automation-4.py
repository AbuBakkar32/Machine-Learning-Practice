from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
driver.get("http://studentportal.diu.edu.bd/#/dashboard")
print(driver.current_url)
print(driver.title)

# time.sleep(5)
driver.close()
driver.quit()

print('Thank for logged-in our website')