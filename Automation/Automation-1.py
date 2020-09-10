from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
browser.maximize_window()
browser.implicitly_wait(3)

browser.get("https://opensource-demo.orangehrmlive.com/")
browser.find_element_by_id('txtUsername').send_keys('Admin')
browser.find_element_by_id('txtPassword').send_keys('admin123')
browser.find_element_by_id('btnLogin').click()
browser.find_element_by_id('welcome').click()


# browser.find_element_by_xpath("//td[text()='Logout']").click()
# try:
#     browser.find_element(By.XPATH("//a[@href='/index.php/auth/logout']")).click()
# except :
#     print("something went wrong")

time.sleep(5)
browser.close()
browser.quit()
print('Thank for logged-in our website')

