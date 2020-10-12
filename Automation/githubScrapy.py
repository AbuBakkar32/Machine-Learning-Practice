from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

browser = webdriver.Chrome('G:/Machine Learning Practice/Automation/driver/chromedriver.exe')
browser.maximize_window()

# browser.get("https://github.com/TheDancerCodes")
# # find_elements_by_xpath returns an array of selenium objects.
# titles_element = browser.find_elements_by_xpath("//a[@class ='text-bold']")
# # use list comprehension to get the actual repo titles and not the selenium objects.
# titles =[x.text for x in titles_element]
# # print out all the titles.
# print('titles:')
# print(titles, '\n')
#
# language_element = browser.find_elements_by_xpath("//p[@class=’mb-0 f6 text-gray’]")
# # same concept as for list-comprehension above.
# languages = [x.text for x in language_element]
# print("languages:")
# print(languages, '\n')
#
# for title, language in zip(titles, languages):
#     print("RepoName : Language")
#     print(title + ": " + language, '\n')

# user_message = browser.find_elements_by_xpath('//*[@id="Comment_5561090"]/div/div[3]/div/div[1]')[0]
# comment = user_message.text
#
# ids = browser.find_elements_by_xpath("//*[contains(@id,'Comment_')]")
# comment_ids = []
# for i in ids:
#     comment_ids.append(i.get_attribute('id'))


# browser.get('https://forums.edmunds.com/discussion/43315/mercedes-benz/amg-gt/amg-gt-leasing-questions')
# userid_element = browser.find_element_by_xpath('//*[@id="Item_0"]/h1')
# print(userid_element.text)
#
#
# user_date = browser.find_element_by_xpath('//*[@id="Discussion_43315"]/div/div[2]/div/div[1]')
# print(user_date.text)


browser.get("https://forums.edmunds.com/discussion/43315/mercedes-benz/amg-gt/amg-gt-leasing-questions")
# elems = browser.find_elements_by_xpath("//a[@href]")

elems = browser.find_elements_by_tag_name('a')
for elem in elems:
    href = elem.get_attribute('href')
    if href is not None:
        print(href)

# browser.close()
# browser.quit()