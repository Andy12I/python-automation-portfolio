import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Setup the "Driver" (The Robot)
# This line automatically downloads the correct driver for your Chrome version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 2. Give orders
print("Opening Google...")
driver.get("https://www.google.com")

# 3. Wait! 
# If we don't add this, Python will finish the script and close the browser INSTANTLY.
print("I will keep the browser open for 30 seconds...")
time.sleep(30) 

print("Closing browser now.")
driver.quit()