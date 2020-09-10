from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.expedia.com/")
driver.find_element_by_link_text('Flights').click()

driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[1]/div/div/div/button').send_keys('SFO')
driver.find_element_by_id('location-field-leg1-destination-input').send_keys('NYC')

time.sleep(2)
# driver.close()
# driver.quit()

