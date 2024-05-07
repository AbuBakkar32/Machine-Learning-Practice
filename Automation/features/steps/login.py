import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I am on the OrangeHRM login page')
def loginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('I enter username "{user}" in the user field')
def enterUsername(context, user):
    context.driver.find_element(By.XPATH,
                                "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
        user)
    time.sleep(2)


@when('I enter password "{pwd}" in the password field')
def enterPassword(context, pwd):
    context.driver.find_element(By.XPATH,
                                "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
        pwd)
    time.sleep(2)


@when('I click the on Login button')
def clickLogin(context):
    context.driver.find_element(By.XPATH,
                                "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()



@then('I should see the Dashboard page')
def verifyDashboard(context):
    dashboard = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    assert dashboard == "Dashboard"
