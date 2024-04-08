import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the Chrome WebDriver
driver = webdriver.Chrome()

# Open the web page
driver.get("http://localhost:3000")

# Wait for the page to load
driver.implicitly_wait(10)

# Click on the signup tab
signup_tab = driver.find_element("id","signupTesting")
signup_tab.click()

# Find input fields
name_field = driver.find_element("id","name")
email_field = driver.find_element("id","email")
password_field = driver.find_element("id","password")
contact_field = driver.find_element("id","contact")

# Fill in signup form fields
name_field.send_keys("TestUser")
email_field.send_keys("test@gmail.com")
password_field.send_keys("AsDr1234!")
contact_field.send_keys("1234567890")

WebDriverWait(driver, 100).until(EC.element_to_be_clickable(('id', 'signupTesting')))

print("Signup test performing!")


input("Press Enter to close the browser window.")

