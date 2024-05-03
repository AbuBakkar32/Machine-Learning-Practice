import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Initialize a Selenium webdriver (you may need to specify the path to your webdriver)
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(3)

# Navigate to the webpage where you want to perform drag and drop
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

# Find the draggable element
draggable_element = driver.find_element(by="id", value="draggable")

# Find the droppable element
droppable_element = driver.find_element(by="id", value="droppable")

# Create an ActionChains object
actions = ActionChains(driver)

# Perform drag and drop operation
actions.drag_and_drop(draggable_element, droppable_element).perform()

# set time for wait
time.sleep(3)

# Close the Selenium webdriver
driver.quit()
