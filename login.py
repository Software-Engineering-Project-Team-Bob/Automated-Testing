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

# Find and click on the login button
login_button = driver.find_element('id','loginTesting')
login_button.click()

# Find email and password fields
email_field = driver.find_element('id','email')
password_field = driver.find_element('id','password')

# Fill in email and password fields
email_field.send_keys("test@example.com")
password_field.send_keys("testpassword")

WebDriverWait(driver, 100).until(EC.element_to_be_clickable(('id', 'loginTesting')))

print("Login test performing !")
    
input("Press Enter to close the browser window.")