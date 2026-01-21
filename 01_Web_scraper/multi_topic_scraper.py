from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from datetime import datetime

# Target list
topics = ["Python (programming language)", "Java (programming language)", "Linux"]

driver = webdriver.Chrome()

# Open file
with open("multi_wiki_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link", "Date Scraped"])

    for topic in topics:
        print(f"--- Scrapping: {topic} ---")

        driver.get("https://www.wikipedia.org")

        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(topic)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        try:
            # Scrape
            article_title = driver.find_element(By.ID, "firstHeading").text
            current_url = driver.current_url
            today = datetime.now().strftime("%d/%m/%Y")

            # Write to CSV
            writer.writerow([article_title, current_url, today])
            print(f"Saved: {article_title}")

        except Exception as e:
            print(f"Failed to scrape {topic}: {e}")

# End
print("All done!")
driver.quit()