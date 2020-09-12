from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(2)

# driver.get("http://studentportal.diu.edu.bd/#/result")
# driver.find_element_by_name('studentId').send_keys('171-35-1994')
# data = driver.find_elements_by_id('select_container_3')
# # print(len(data))
# time.sleep(2)

driver.get("https://www.facebook.com/")
driver.find_element_by_id('u_0_2').click()
time.sleep(1)
driver.find_element_by_name('firstname').send_keys('Abu Bakkar')
time.sleep(1)
driver.find_element_by_id('u_1_d').send_keys('Siddik')
time.sleep(1)
driver.find_element_by_name('reg_email__').send_keys('absrakib1@gmail.com')
time.sleep(1)
driver.find_element_by_name('reg_email_confirmation__').send_keys('absrakib1@gmail.com')
time.sleep(1)
driver.find_element_by_name('reg_passwd__').send_keys('AbuBakkar32')
time.sleep(1)
driver.find_elements_by_tag_name('option')[1].click()
time.sleep(1)
driver.find_elements_by_tag_name('option')[33].click()
time.sleep(1)
driver.find_elements_by_tag_name('option')[68].click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_1_5"]').click()

time.sleep(1)
driver.find_element_by_name('websubmit').click()


# el = driver.find_element_by_id('id_of_select')
# for option in el.find_elements_by_tag_name('option'):
#     if option.text == 'The Options I Am Looking For':
#         option.click() # select() in earlier versions of webdriver
#         break

# driver.close()
# driver.quit()
print('Thank for logged-in our website')