from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import time

# Ghost Configuration
chrome_options = Options()
chrome_options.add_argument("--headless=new") # Invisible command

print("---Starting the Ghost Driver ---")
# Passing on to driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://books.toscrape.com/")

# Proof (The Screenshot)
# picture verifies the bot is working
print("Taking a screenshot...")
driver.save_screenshot("ghost_evidence.png") # <---- Save an image of the page

# ---- 3. The Scrape ----
book_cards = driver.find_elements(By.CLASS_NAME, "product_pod")
print(f"Ghost found {len(book_cards)} books!")

with open("headless_data.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])

    for card in book_cards:
        try:
            header = card.find_element(By.TAG_NAME, "h3")
            full_title = header.find_element(By.TAG_NAME, "a").get_attribute("title")
            price = card.find_element(By.CLASS_NAME, "price_color").text

            writer.writerow([full_title, price])

        except Exception as e:
            print(f"Error: {e}")

print("Success! Check 'ghost_evidence.png' and 'headless_data.csv'")
driver.quit()