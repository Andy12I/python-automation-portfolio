import requests
from bs4 import BeautifulSoup
import csv
import os
print(f"I am saving files to this folder: {os.getcwd()}")

# Function 1: Connect
def get_soup(url):
    print(f"Connecting to {url}...")
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")

# Function 2: Extract
def extract_quotes(soup):
    quotes_list = soup.find_all("span", class_="text")
    return quotes_list

# ---- Main execution ----
# Get the soup, Get the Quotes and pass to Function
all_quotes = []

# range(1,6) gives us numbers 1,2,3,4,5
for i in range(1, 6):
    # The Dynamic url
    url = f"http://quotes.toscrape.com/page/{i}/"

    # 2. Get the soup
    current_soup = get_soup(url)

    # 3. Extract quotes
    current_quotes = extract_quotes(current_soup)

    # 4. Add to the bucket
    all_quotes = all_quotes + current_quotes

    print(f"✅ Scraped page {i}")

    # --- Final Report ---
    print(f"Total quotes found: {len(all_quotes)}")

# Saving to file
print("Saving data to file...")
with open("my_scrapped_quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write the Header Row
    writer.writerow(["Quote Text"])
    for quote in all_quotes:
        writer.writerow([quote.text])

print("Success! Open file to see Data.")    