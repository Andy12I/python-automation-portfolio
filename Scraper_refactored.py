import requests
from bs4 import BeautifulSoup

# --- THE HELPER FUNCTION ---
def get_soup(url):
    print(f"Connecting to {url}...")
    page = requests.get(url)
    # Create the soup
    soup = BeautifulSoup(page.text, "html.parser")
    # HAND THE SOUP BACK!
    return soup 

# --- THE MAIN CODE ---
# We don't need to see the requests or bs4 setup logic here anymore.

# 1. Use the function
my_soup = get_soup("http://quotes.toscrape.com")

# 2. Extract quotes (Just like before)
quotes = my_soup.find_all("span", class_="text")

print(f"Found {len(quotes)} quotes.")