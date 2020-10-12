from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
browser.maximize_window()
browser.implicitly_wait(3)
for _ in range(1, 4):
    browser.get("https://opensource-demo.orangehrmlive.com/")
    browser.find_element_by_id('txtUsername').send_keys('Admin')
    browser.find_element_by_id('txtPassword').send_keys('admin123')
    browser.find_element_by_id('btnLogin').click()
    browser.find_element_by_id('welcome').click()
    browser.find_element_by_link_text('Logout').click()
    time.sleep(4)

# admin = browser.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
# usermng = browser.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
# user = browser.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

# action = ActionChains(browser)
# action.move_to_element(admin).move_to_element(usermng).move_to_element(user).click().perform() # this is for move element action
# action.double_click(admin).perform() # this is for Double click action
# action.context_click(admin) # this is for right click action
# action.drag_and_drop(source, destination) # this is for Drag and drop action


time.sleep(5)
# browser.close()
# browser.quit()
print('Thank for logged-in our website')
