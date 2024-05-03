from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
email = 'abubakkarsiddik32@hotmail.com'
password = 'AbuBakkar'

driver.get("https://www.facebook.com/")
driver.find_element(by='id', value='email').send_keys(email)
driver.find_element(by='id', value='pass').send_keys(password)
driver.find_element(by='name', value='login').click()

# browser.find_element_by_xpath('//*[@id="js_0"]/div/div/div[2]/div/div/a').click()
# Xpath=//*[contains(@id,'message')]
# Xpath=//label[starts-with(@id,'message')]
# Xpath=//td[text()='UserID']
time.sleep(2)

# browser.close()
# browser.quit()
print('Thank for logged-in our website')