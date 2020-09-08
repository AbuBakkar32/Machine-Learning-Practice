from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
browser.maximize_window()
email = 'abubakkarsiddik32@hotmail.com'
password = 'AbuBakkar'

browser.get("https://www.facebook.com/")
browser.find_element_by_id('email').send_keys(email)
browser.find_element_by_id('pass').send_keys(password)
browser.find_element_by_name('login').click()

# browser.find_element_by_xpath('//*[@id="js_0"]/div/div/div[2]/div/div/a').click()
# Xpath=//*[contains(@id,'message')]
# Xpath=//label[starts-with(@id,'message')]
# Xpath=//td[text()='UserID']
time.sleep(2)

# browser.close()
# browser.quit()
print('Thank for logged-in our website')