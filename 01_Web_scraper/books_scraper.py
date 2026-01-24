from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# 1. Setup
driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")
book_cards = driver.find_elements(By.CLASS_NAME, "product_pod")

print(f"Found{len(book_cards)} books. Starting scrape ...")

# Open CSV
with open ("books_data.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])

    for card in book_cards:
        try:
            header = card.find_element(By.TAG_NAME, "h3")
            link = header.find_element(By.TAG_NAME, "a")

            full_title = link.get_attribute("title")

            price = card.find_element(By.CLASS_NAME, "price_color").text

            writer.writerow([full_title,price])
            print(f"Scraped: {full_title}")

        except Exception as e:
            print(f"Error scraping a book: {e}")

driver.quit()