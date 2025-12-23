import requests
from bs4 import BeautifulSoup

# Function 1: Connect
def get_soup(url):
    print(f"Connecting to {url}...")
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")

# Function 2: Extract

def extract_quotes(soup):
    quotes_list = soup.find_all("span", class_="text")
    return quotes_list

# --- MAIN EXECUTION ---
# 1. Get the soup, Get the quotes (Pass my_soup into new funtion)
soup1 = get_soup("http://quotes.toscrape.com")
quotes1 = extract_quotes(soup1)
print(f"Page 1 Extraction complete, Found {len(quotes1)} quotes")

# 2. Doing the same for page 2
soup2 = get_soup("http://quotes.toscrape.com/page/2/")
quotes2 = extract_quotes(soup2)
print(f"Page 2 Extraction complete, Found {len(quotes2)} quotes")


# 3. Print results
print("---Starting the Loop---")
count = 0
for quote in quotes1 + quotes2:
                count = count + 1
                print(f"{count}.{quote.text}...")
                print(f"--- Total Printed: {count}")