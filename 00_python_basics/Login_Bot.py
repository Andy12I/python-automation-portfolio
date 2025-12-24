import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print("Navigating to SauceDemo...")
driver.get("https://www.saucedemo.com/")

# 1. Find Username box and type
# Hint: Use driver.find_element(By.ID, "what_is_the_id?")
# You must inspect the page to find the ID!
user_box = driver.find_element(By.ID, "user-name") 
user_box.send_keys("standard_user")

# 2. Find Password box and type
pass_box = driver.find_element(By.ID, "password")
pass_box.send_keys("wrong_password")

# 3. Find Login Button and Click
# Hint: .click() works just like .send_keys()
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
# 1. Wait a moment for the page to load
time.sleep(2)

# 2. Get the current address from the browser
current_address = driver.current_url

# 3. VERIFY
# We check if the word "inventory" is inside the URL
if "inventory" in current_address:
    print("✅ TEST PASSED: We are in the store!")
    print("Login successful! Pausing for 10 seconds.")
else:
    print(f"❌ TEST FAILED: Still stuck at {current_address}") 


time.sleep(10)
driver.quit()