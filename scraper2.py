import requests
from bs4 import BeautifulSoup
import csv


url = "http://quotes.toscrape.com"
page = requests.get(url)
print(f"Status Code: {page.status_code}")

soup = BeautifulSoup(page.text, "html.parser")
quotes = soup.find_all("span", class_="text")
print(f"I found {len(quotes)} quotes on this page!\n")

with open("quotes.csv", "w", newline='') as file:
    my_writer = csv.writer(file)
    my_writer.writerow(["Quote list"])
   
    for quote in quotes:
     clean_text = quote.text
     my_writer.writerow([clean_text])

print("Saved to quotes.csv sucessfully!")