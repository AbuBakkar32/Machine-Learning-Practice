import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.implicitly_wait(2)

browser.get("https://www.instagram.com/")

fb_mail = "rakibsarkar26@gmail.com"
fb_pass = "AbuBakkar@32"
list_of_user = ['abubakkarsiddik32', 'imranfahim.mkt16']

browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[5]/button/span[2]').click()
browser.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(fb_mail)
browser.find_element(by=By.XPATH, value='//*[@id="pass"]').send_keys(fb_pass)
browser.find_element(by=By.XPATH, value='//*[@id="loginbutton"]').click()
browser.implicitly_wait(5)

pyautogui.moveTo(679, 561)
time.sleep(25)
x, y = pyautogui.position()
time.sleep(2)
pyautogui.click(x, y)

if len(list_of_user) > 0:
    for user in list_of_user:
        # find the search option then click on it and write a user name
        pyautogui.moveTo(600, 150)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.write(user)

        # click on user that i have searched
        time.sleep(2)
        pyautogui.moveTo(650, 210)
        x, y = pyautogui.position()
        time.sleep(1)
        pyautogui.click(x, y)

        # click user post
        time.sleep(2)
        pyautogui.moveTo(320, 680)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(2)

        # click on message button
        pyautogui.moveTo(862, 690)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.write("Thanks for following")
        time.sleep(1)

        pyautogui.moveTo(1180, 680)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(2)

        pyautogui.moveTo(1320, 140)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(2)

        pyautogui.moveTo(250, 140)
        x, y = pyautogui.position()
        pyautogui.click(x, y)

    print("----------------Thank for using our Bot-----------")
else:
    print('Sorry User Not Found')
