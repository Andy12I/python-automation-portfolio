import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Setup
Service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service, options=chrome_options)

print("Navigating to SauceDemo...")
driver.get("https://www.saucedemo.com")

# 1. Find Username box and type
# You must inspect the page to find the ID!
user_box = driver.find_element(By.ID, "user-name")
user_box.send_keys("standard_user")

# 2. Find the password box and type
pass_box = driver.find_element(By.ID, "password")
pass_box.send_keys("secret_sauce")

# 3. Find Login Button and Click
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
# Wait a moment for the page to load
time.sleep(2)

# 4. Get the current address from the browser
current_address = driver.current_url

# 5. Verify
if "inventory" in current_address:
    print("✅ Test passed!")
    print("Login successful, Pausing for 10 seconds")
else:
    print("❌ Login Failed")

time.sleep(10)