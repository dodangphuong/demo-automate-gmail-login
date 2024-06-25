from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

class Google:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Corrected path handling
        service = Service(r'C:\Dev\WebDrivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
    
    def login(self):
        # Open Gmail
        self.driver.get("https://mail.google.com/")

        # Wait for the email field and enter your email
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
        )
        email_field.send_keys(self.username)
        email_field.send_keys(Keys.RETURN)

        # Wait for the password field and enter your password
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="password"]'))
        )
        time.sleep(2)  # Sleep for a few seconds to allow transition (optional)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

        # Wait for the inbox to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@role="main"]'))
        )

        print("Logged in successfully!")
        # Close the browser
        self.driver.quit()

# Retrieve credentials from environment variables for security
user = open('New Text Document (1).txt',"r", encoding="utf-8")
username = str(user.read())
pwd = open('New Text Document.txt',"r", encoding="utf-8")
password = str(pwd.read())
# Ensure that the credentials are available
if username is None or password is None:
    raise Exception("Please set the GMAIL_USER and GMAIL_PASS environment variables")

# Create an instance of Google and log in
PhuongDepTrai = Google(username, password)
PhuongDepTrai.login()
