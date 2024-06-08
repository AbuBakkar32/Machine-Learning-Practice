"""
Author: Abu Bakkar Siddikk
Date: 2024-06-08
Description: This script automates the process of creating a When2Meet event, signing in with a specified name, and marking availability from 10 AM to 11 AM for each day.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def create_event(driver):
    # Set the date range (15-20 June)
    for week in range(1, 6):
        for day in range(1, 6):
            if week == 2:
                driver.find_element(By.ID, f"Day-{week}-7").click()
            if week == 3:
                driver.find_element(By.ID, f"Day-3-{day}").click()

    # Enter event name
    event_name_field = driver.find_element(By.ID, "NewEventName")
    event_name_field.clear()
    event_name_field.send_keys("Test Event")

    # Set the time range (8 AM to 6 PM)
    start_time_field = driver.find_element(By.NAME, "NoEarlierThan")
    start_time_field.click()
    start_time_field.send_keys("8:00 AM")
    start_time_field.send_keys(Keys.RETURN)

    end_time_field = driver.find_element(By.NAME, "NoLaterThan")
    end_time_field.click()
    end_time_field.send_keys("6:00 PM")
    end_time_field.send_keys(Keys.RETURN)

    # Create the event
    create_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    create_button.click()


def sign_in(driver):
    time.sleep(2)  # Allow time for the page to load
    driver.find_element(By.ID, "name").send_keys("Abu Bakkar Siddikk")
    driver.find_element(By.CSS_SELECTOR, "input[value='Sign In']").click()

    # Wait for the availability grid to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "YouGrid")))


def mark_availability(driver):
    # Wait for the availability grid to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "YouGrid"))
    )
    time.sleep(2)  # Allow time for the grid to become interactive
    grid_cells = driver.find_element(By.ID, "YouGridSlots")
    every_div = grid_cells.find_elements(By.TAG_NAME, "div")
    action_chains = ActionChains(driver)

    for cell in every_div[50:110]:
        for div in cell.find_elements(By.TAG_NAME, "div"):
            action_chains.move_to_element(div).click().perform()
            time.sleep(0.1)


# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Create When2Meet event with date range of 15-20 June from 8 AM to 6 PM.
    driver.get("https://www.when2meet.com/")
    driver.maximize_window()
    create_event(driver)

    # Step 2: Sign in using a specified name
    sign_in(driver)

    # Step 3: Mark availability from 10 AM to 11 AM for each day
    mark_availability(driver)

    print("Availability has been marked successfully.")

finally:
    time.sleep(5)  # Pause to see the result before closing
    driver.quit()
