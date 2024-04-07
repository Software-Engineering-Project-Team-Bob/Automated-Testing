import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the Chrome WebDriver
driver = webdriver.Chrome()

# Open the web page
driver.get("http://localhost:4000")

# Print a message prompting the user to manually navigate to the page with the join button
print("Please manually navigate to the page with the join button and click it.")

# Wait for the user to confirm that they have clicked the join button
input("Press Enter after clicking the join button manually.")

# Find the class code input field
class_code_field = driver.find_element('id', 'classCode')

# Fill in the class code input field
class_code_field.send_keys("123478")  # Assuming the class code is "123456"

# Find and click the join button
join_button = driver.find_element('id', 'JoinClassButton')
# join_button.click()

print("Join classroom test performing!")

input("Press Enter after confirming that the classroom was joined successfully.")

# You can add assertions here to verify if the classroom was successfully joined

# Close the browser session
driver.quit()
