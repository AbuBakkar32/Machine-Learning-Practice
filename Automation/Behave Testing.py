from behave import *
from selenium.webdriver.common.keys import Keys

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


@given('the DuckDuckGo home page is displayed')
def step_impl(context):
    context.browser.get(DUCKDUCKGO_HOME)


@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    search_input = context.browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


@then('results are shown for "{phrase}"')
def step_impl(context, phrase):
    links_div = context.browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = context.browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
