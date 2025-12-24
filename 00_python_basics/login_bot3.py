import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
Service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service, options=chrome_options)

print("Navigating to Saucedemo.com..")
driver.get("https://www.saucedemo.com")

# Define the smart wait (max 10 seconds)
wait = WebDriverWait(driver, 10)
print("Waiting for username box...")

# Instead of find_element, wait for it to appear
user_box = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
user_box.send_keys("standard_user")

# Do the same for password ...
pass_box = wait.until(EC.presence_of_element_located((By.ID, "password")))
pass_box.send_keys("secret_sauce")

# Do the same for Login Button...
login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()
print("Clicked! Waiting for inventory page to load...")

# Check URl
current_address = driver.current_url
try:
    wait.until(EC.url_contains("inventory"))
    print("✅ Success!")
except:
    print("❌ Fail! Url never changed.")
    print(f"Current URL is: {driver.current_url}")

time.sleep(2)