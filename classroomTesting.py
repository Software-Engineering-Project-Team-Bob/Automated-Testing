import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the Chrome WebDriver
driver = webdriver.Chrome()

# try:
# Open the web page
driver.get("http://localhost:4000")

# Wait for the page to load
# driver.implicitly_wait(1000)
# Print a message prompting the user to manually navigate to the desired page
print("Please manually navigate to the page with the create button and click it.")

# Wait for the user to confirm that they have clicked the button
input("Press Enter after clicking the create button manually.")


# Find classroom creation form fields
class_name_field = driver.find_element('id', 'classname')
description_field = driver.find_element('id', 'description')
field_name_field = driver.find_element('id', 'field')
class_level_field = driver.find_element('id', 'classlevel')
meet_link_field = driver.find_element('id', 'meetlink')

# Fill in classroom creation form fields
class_name_field.send_keys("Test Classroom")
description_field.send_keys("This is a test classroom.")
field_name_field.send_keys("Test Field")
class_level_field.send_keys("Test Level")
meet_link_field.send_keys("https://meet.google.com/test-meeting-link")

# Submit the form
create_button = driver.find_element('id', 'createClassroomButton')
# create_button.click()

print("Classroom creation test performing!")

input ("Press Enter to close the browser window.")

driver.quit()

# You can add assertions here to verify if the classroom was successfully created

# except Exception as e:
#     print("An error occurred during testing:", e)

# finally:
#     # Close the browser session
#     driver.quit()
