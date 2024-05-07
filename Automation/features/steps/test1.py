from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open the OrangeHRM Home Page')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


@then('verify the logo on the page')
def verify_logo(context):
    context.driver.implicitly_wait(10)
    logo = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[1]/img")
    assert logo.is_displayed() is False


@then('close browser')
def close_browser(context):
    context.driver.close()
