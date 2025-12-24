import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# NEW IMPORTS
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Start the Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print("Opening Google...")
driver.get("https://www.google.com")

# 2. Find the Search Bar
# We look for the element where name="q"
search_box = driver.find_element(By.NAME, "q")

# 3. Type inside it
print("Typing search query...")
search_box.send_keys("Python QA jobs remote")

# 4. Press Enter
# We simulate pressing the 'Return' (Enter) key
time.sleep(1) # Wait 1 second just to look human
search_box.send_keys(Keys.RETURN)

print("Search complete! Leaving open for 10 seconds...")
time.sleep(10)
driver.quit()